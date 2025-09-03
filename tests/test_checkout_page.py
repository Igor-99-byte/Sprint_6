import pytest
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from locators.ordercomplite_page_locators import OrderComlitePageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from utils.data import test_cases_complete
import allure
import time

@pytest.mark.usefixtures("browser")
class TestCheckout:
    @pytest.mark.parametrize("name,last_name,adres,metro,phone,when,days,comm", test_cases_complete)
    @allure.story("Проверка успешного оформления заказа")
    @allure.title("Тест оформления заказа с данными")
    def test_checkout_page(self, name, last_name, adres, metro, phone, when, days, comm):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.click_button_up()
        checkout_page.fill_first_page_form(name, last_name, adres, metro, phone)
        checkout_page.click_button_next()
        checkout_page.fill_second_page_form(when, days, comm)
        checkout_page.click_order()
        checkout_page.click_yes()
        wait = WebDriverWait(self.driver, 10)
        success_element = wait.until(
        EC.visibility_of_element_located(OrderComlitePageLocators.NAME)
    )
    
        actual_text = success_element.text
        assert "Заказ оформлен" in actual_text

        checkout_page.click_status()
        checkout_page.click_scuter()
        assert self.driver.find_element(MainPageLocators.SCUTER).is_displayed()

        checkout_page.click_yandex()
        time.sleep(2)
        current_url = self.driver.current_url
        assert "dzen.ru" in current_url
        