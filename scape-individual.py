from bs4 import BeautifulSoup
import urllib2
import mechanize
import cookielib

# r = urllib.urlopen('https://colleges.niche.com/arizona-state-university/rankings/').read()
# soup = BeautifulSoup(r)

soup = BeautifulSoup(open('/Users/ellliottribner/development/admit_hub/colleges-niche/local-sample-asu.html'))

name = soup.find('h1', {"itemprop": "name"}).find('a').text
overall_grade = soup.find("div", { "class" : "overall-grade" })["class"][2]
# town = soup.find('span', {"itemprop": "addressLocality"})
# state = soup.find('span', {"itemprop": "addressRegion"})

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
	categoryStats[categoryTitle] = categoryGrade 

masterHash = { "name": name, "overall-grade": overall_grade, "headerStats": headerStats, "categoryStats": categoryStats }
print masterHash