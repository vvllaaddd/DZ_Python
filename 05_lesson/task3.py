from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открываем браузер
browser = webdriver.Firefox()
browser.get("http://the-internet.herokuapp.com/inputs")

time.sleep(2)  # Ждем загрузку страницы

# Находим поле ввода
input_field = browser.find_element(By.TAG_NAME, "input")

# Вводим текст "Sky"
input_field.send_keys("Sky")
time.sleep(1)

# Очищаем поле
input_field.clear()
time.sleep(1)

# Вводим текст "Pro"
input_field.send_keys("Pro")
time.sleep(1)

# Закрываем браузер
browser.quit()
