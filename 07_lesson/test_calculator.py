import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


def test_open_calc_page(driver):
    calc = CalculatorPage(driver)

    calc.set_delay(45)

    for key in ["7", "+", "8", "="]:
        calc.click_button(key)

    result = calc.wait_for_result("15")
    assert result == "15", f"Ожидался результат '15', но получено: {result}"
