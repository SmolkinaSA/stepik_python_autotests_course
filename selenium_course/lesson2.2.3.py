from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = int(browser.find_element(By.ID, "num1").text)
num2 = int(browser.find_element(By.ID, "num2").text)
result = num1 + num2

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(result))

button = browser.find_element(By.XPATH, "//*[text()='Submit']")
button.click()

time.sleep(30)
browser.quit()