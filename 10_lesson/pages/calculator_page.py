from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: WebDriver — экземпляр веб-драйвера браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay: int):
        """
        Устанавливает задержку выполнения операций калькулятора.

        :param delay: int — значение задержки в секундах.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button_text: str):
        """
        Нажимает на кнопку с заданным текстом.

        :param button_text: str — текст на кнопке.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_text}']")
            )
        )
        button.click()

    def wait_for_result(self, expected_result: str, timeout: int = 50) -> str:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param expected_result: str — ожидаемый текст результата.
        :param timeout: int — максимальное время ожидания.
        :return: str — текст результата на экране.
        """
        result_screen = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "screen"))
        )
        WebDriverWait(self.driver, timeout).until(
            lambda d: result_screen.text.strip() == expected_result
        )
        return result_screen.text.strip()
