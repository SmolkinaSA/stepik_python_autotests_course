from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # Ваш код, который заполняет обязательные поля
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys("mail@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]')
    input4.send_keys("1234567890")
    input5 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
    input5.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()