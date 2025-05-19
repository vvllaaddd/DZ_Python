import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """
    Страница с товарами после авторизации.
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step("Добавление товара с ID: {item_id} в корзину")
    def add_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по ID.
        """
        self.driver.find_element(By.ID, item_id).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
