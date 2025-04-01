from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    # Ожидание появления текста "Done!"
    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "text"),
            "Done!"
        )
    )

    # После появления "Done!" ищем все картинки
    images = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "img")
        )
    )

    # Проверяем, есть ли 3 изображения
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print(third_image_src)
    else:
        print("На странице недостаточно изображений.")

finally:
    driver.quit()
