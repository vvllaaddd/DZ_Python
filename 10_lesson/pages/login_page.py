import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    Страница авторизации на сайте saucedemo.com.
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Вход в систему под пользователем '{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Авторизация пользователя и попытка закрытия всплывающего окна.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        self.close_password_reset_popup()

    @allure.step("Проверка наличия и закрытие всплывающего окна смены пароля")
    def close_password_reset_popup(self) -> None:
        """
        Закрывает всплывающее окно, если оно появляется.
        """
        try:
            reset_btn = self.driver.find_element(By.CLASS_NAME, "error-button")
            reset_btn.click()
        except NoSuchElementException:
            pass
