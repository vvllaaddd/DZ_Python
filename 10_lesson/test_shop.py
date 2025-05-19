import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver() -> WebDriver:
    """
    Фикстура для запуска и завершения сессии браузера Chrome.
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.feature("Покупка товаров")
@allure.story("Проверка итоговой суммы заказа")
def test_total_price(driver: WebDriver) -> None:
    """
    Тест проверяет, что итоговая сумма заказа корректна после добавления
    нескольких товаров.
    """
    login = LoginPage(driver)
    with allure.step("Авторизация пользователя standard_user"):
        login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    with allure.step("Добавление товаров в корзину"):
        inventory.add_to_cart("add-to-cart-sauce-labs-backpack")
        inventory.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        inventory.add_to_cart("add-to-cart-sauce-labs-onesie")
        inventory.go_to_cart()

    cart = CartPage(driver)
    with allure.step("Переход к оформлению заказа"):
        cart.click_checkout()

    checkout = CheckoutPage(driver)
    with allure.step("Заполнение формы и получение итоговой суммы"):
        checkout.fill_form("Vladislav", "Vladislav", "162100")
        total = checkout.get_total()

    expected = "Total: $58.29"
    assert total == expected, (
        f"Ожидался результат '{expected}', но получено: {total}"
    )
