import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """
    Страница корзины покупок.
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step("Нажатие кнопки Checkout")
    def click_checkout(self) -> None:
        """
        Кликает по кнопке оформления заказа (Checkout).
        """
        self.driver.find_element(By.ID, "checkout").click()
