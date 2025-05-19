import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Страница оформления заказа (Checkout).
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step(
        "Заполнение формы с данными: {first_name} {last_name}, "
        "индекс: {postal_code}"
    )
    def fill_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет форму заказа и нажимает кнопку Continue.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total(self) -> str:
        """
        Ожидает и возвращает текст с итоговой суммой заказа.
        """
        total_label = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_label.text.strip()
