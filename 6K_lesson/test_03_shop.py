import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажатие на кнопку Checkout
    driver.find_element(By.ID, "checkout").click()

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("vladislav")
    driver.find_element(By.ID, "last-name").send_keys("vladislav")
    driver.find_element(By.ID, "postal-code").send_keys("162100")

    # Нажать кнопку Continue
    driver.find_element(By.ID, "continue").click()

    # Прочитать итоговую стоимость
    total_label = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_label.text.strip()

    # Проверка, что итоговая сумма равна $58.29
    assert total_text == "Total: $58.29", \
        f"Ожидался результат 'Total: $58.29', но получено: {total_text}"

    # Закрытие браузера
    driver.quit()
