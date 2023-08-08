from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

chest = browser.find_element(By.ID, "treasure")

chest_valuex = chest.get_attribute("valuex")
print("value of chest: ", chest_valuex)
assert chest_valuex is not None

result = calc(chest_valuex)

option1 = browser.find_element(By.CSS_SELECTOR, "[type='text']")
option1.send_keys(result)
option2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
option2.click()
option3 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
option3.click()

button = browser.find_element(By.XPATH, "//*[text()='Submit']")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()