from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://colleges.niche.com/login.aspx")

elem = driver.find_element_by_name("ctl00$MainContentPlaceholder$EmailAddress")
elem.send_keys("elliott.ribner@techstars.com")

elem2 = driver.find_element_by_name("ctl00$MainContentPlaceholder$Password")
elem2.send_keys('password')

submitButton = driver.find_element_by_name("ctl00$MainContentPlaceholder$LoginButton")
submitButton.click()

driver.close()


