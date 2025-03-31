from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Открываю браузер
driver = webdriver.Chrome()

# Перехожу на сайт
driver.get("http://uitestingplayground.com/classattr")

# Нахожу кнопку по классу
button = driver.find_element(By.CLASS_NAME, "btn-primary")

# Кликаю по кнопке
button.click()

# Делаю паузу, чтобы увидеть результат
sleep(3)
