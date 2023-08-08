from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text

result = calc(x)

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