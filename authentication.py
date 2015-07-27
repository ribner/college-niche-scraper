# import mechanize
# from bs4 import BeautifulSoup
# import urllib2 
# import cookielib


# cj = cookielib.CookieJar()
# br = mechanize.Browser()
# br.set_cookiejar(cj)
# r = br.open('http://colleges.niche.com/login.aspx')
# html = r.read()
# br.select_form(name="aspnetForm")
# print html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://colleges.niche.com/login.aspx")
# assert "Python" in driver.title
elem = driver.find_element_by_name("ctl00$MainContentPlaceholder$EmailAddress")
elem.send_keys("elliott.ribner@techstars.com")

elem2 = driver.find_element_by_name("ctl00$MainContentPlaceholder$Password")
elem2.send_keys('yourPassword')

submitButton = driver.find_element_by_name("ctl00$MainContentPlaceholder$LoginButton")
submitButton.click()


driver.close()


