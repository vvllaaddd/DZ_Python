import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


def test_open_calc_page(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    wait = WebDriverWait(driver, 10)

    # Ввод значения 45 в поле задержки
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Функция для клика по кнопке
    def click_button(button_text):
        button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_text}']")
            )
        )
        button.click()

    # Последовательность нажатий
    for key in ["7", "+", "8", "="]:
        click_button(key)

    # Ожидание результата "15"
    result_screen = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "screen"))
    )

    WebDriverWait(driver, 50).until(
        lambda d: result_screen.text.strip() == "15"
    )

    assert result_screen.text.strip() == "15", (
        f"Ожидался результат '15', но получено: {result_screen.text}"
    )
