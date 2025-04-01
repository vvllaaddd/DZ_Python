from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Открываем браузер
browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/dynamicid")

sleep(2)  # Ждем загрузку страницы

# Находим кнопку по тексту и кликаем
button = browser.find_element(
    By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]"
)
print("Клик по кнопке выполнен")

sleep(2)  # Немного ждем, чтобы увидеть результат
