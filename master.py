# selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#bs4 and scraping imports
from bs4 import BeautifulSoup
import urllib2
import csv
import time
import json

#login
driver = webdriver.Firefox()
driver.get("http://colleges.niche.com/login.aspx")

elem = driver.find_element_by_name("ctl00$MainContentPlaceholder$EmailAddress")
elem.send_keys("elliott.ribner@techstars.com")

elem2 = driver.find_element_by_name("ctl00$MainContentPlaceholder$Password")
elem2.send_keys('password')

submitButton = driver.find_element_by_name("ctl00$MainContentPlaceholder$LoginButton")
submitButton.click()

#scrape
def getStatsHash(schoolUrl):
	driver.get(schoolUrl)
	time.sleep(5)
	html = driver.page_source
	soup = BeautifulSoup(html)
	name = soup.find('h1', {"itemprop": "name"}).find('a').text
	overall_grade = ""
	try:
		overall_grade = soup.find("div", { "class" : "overall-grade" })["class"][2]
	except:
		print 'error'
	header = soup.find("ul", {"class": "cf"})
	headerCategories = header.find_all('li')
	headerStats = {}

	for i in headerCategories:
		label =  i.find("span", {"class" : "label"})
		value =  i.find("span", {"class" : "value"})
		if label and value:
			labelText = label.text
			valueText = value.text
			headerStats[labelText] = valueText

	categories = soup.find_all("li", { "class" : "ranking-cat" })
	categoryStats = {}
	for i in categories:
		categoryTitle =  i.find('h3').text.strip()
		categoryGrade =  i.find("div", {"class" : "section-grade"})["class"][2]
		rankArray = i.find("div", {"class": "placement"}).text.split(' ')
		if rankArray[0].strip()[0] == '#':
			schoolRank = rankArray[0].strip()
			totalRank = rankArray[2].strip()
		else:
			schoolRank = 'unranked'
			totalRank = 'unranked'
		categoryStats[categoryTitle] = {'category- grade': categoryGrade, 'category-rank': {'school-rank': schoolRank, 'total-rank': totalRank }}

	schoolHash = { "overall-grade": overall_grade, "headerStats": headerStats, "categoryStats": categoryStats }
	return name, schoolHash


masterHash = {}
with open('college-niche.csv') as csvfile:
	filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in filereader:
		name, schoolHash = getStatsHash(row[0])
		masterHash[name] = schoolHash
		with open('college-niche-data.txt', 'w') as outfile:
			json.dump(masterHash, outfile) 

driver.close()

