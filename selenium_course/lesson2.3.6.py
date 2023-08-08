from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открываем страницу
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# Находим и жмакаем нужную кнопку
button1 = browser.find_element(By.XPATH, "//*[text()='I want to go on a magical journey!']")
button1.click()

# Узнаем имя новой вкладки и кладем в переменную
new_window = browser.window_handles[1]
# Переключаемся на новую вкладку
browser.switch_to.window(new_window)

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