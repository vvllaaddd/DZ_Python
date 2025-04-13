from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        self.close_password_reset_popup()

    def close_password_reset_popup(self):
        try:
            reset_btn = self.driver.find_element(By.CLASS_NAME, "error-button")
            reset_btn.click()
        except NoSuchElementException:
            pass
