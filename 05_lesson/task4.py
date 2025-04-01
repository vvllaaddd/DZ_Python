from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открываем браузер
browser = webdriver.Firefox()
browser.get("http://the-internet.herokuapp.com/login")

time.sleep(2)  # Ждем загрузку страницы

# Находим поля ввода и вводим данные
browser.find_element(By.ID, "username").send_keys("tomsmith")
browser.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login
browser.find_element(By.TAG_NAME, "button").click()

time.sleep(2)  # Ждем загрузки страницы

# Выводим текст зеленой плашки
message = browser.find_element(By.ID, "flash").text
print(message)

# Закрываем браузер
browser.quit()
