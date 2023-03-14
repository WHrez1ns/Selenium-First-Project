from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('https://google.com')

element = driver.find_element(By.NAME, "q")
element.send_keys("Vancouver" + Keys.RETURN)
# or "element.submit()"

time.sleep(5)
driver.quit()
