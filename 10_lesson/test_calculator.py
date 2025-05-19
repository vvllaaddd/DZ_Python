import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.title("Проверка калькуляции 7 + 8")
@allure.description(
    "Тест проверяет, что калькулятор правильно считает 7 + 8 при "
    "установленной задержке"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_calc_page(driver):
    with allure.step("Открытие страницы калькулятора"):
        calc = CalculatorPage(driver)

    with allure.step("Установка задержки 45 секунд"):
        calc.set_delay(45)

    with allure.step("Ввод выражения 7 + 8 ="):
        for key in ["7", "+", "8", "="]:
            calc.click_button(key)

    with allure.step("Ожидание и проверка результата"):
        result = calc.wait_for_result("15")
        assert result == "15", (
            f"Ожидался результат '15', но получено: {result}"
        )
