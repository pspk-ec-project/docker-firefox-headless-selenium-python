from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.google.com")
assert "google" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("amazon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
