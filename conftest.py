import pytest
from selenium import webdriver
import allure

@pytest.fixture
def browser(request):
    with allure.step("Настройка браузера"):
        driver = webdriver.Firefox()
        driver.get("https://qa-scooter.praktikum-services.ru/")
        request.cls.driver = driver
    
    yield driver
    
    with allure.step("Завершение работы браузера"):
        driver.quit()