from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Дожидаемся, когда цена дома уменьшится до 100$
price = WebDriverWait(browser, 12).until(
EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

# Нажимаем на кнопку book
button = browser.find_element(By.CSS_SELECTOR, "#book")
button.click()

# Находим элемент с нужным числом и вытаскиваем его для дальнейшего использования
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text

# Найденный Х подставляем в формулку выше
result = calc(x)

# Результат вычисления вставляем в поле ответа
option1 = browser.find_element(By.CSS_SELECTOR, "[type='text']")
option1.send_keys(result)

# Нажимаем отправить
button2 = browser.find_element(By.XPATH, "//*[text()='Submit']")
button2.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()