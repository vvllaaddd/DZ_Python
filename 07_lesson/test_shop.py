import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


def test_total_price(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart("add-to-cart-sauce-labs-backpack")
    inventory.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory.add_to_cart("add-to-cart-sauce-labs-onesie")
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Vladislav", "Vladislav", "162100")
    total = checkout.get_total()

    assert total == "Total: $58.29", \
        f"Ожидался результат 'Total: $58.29', но получено: {total}"
