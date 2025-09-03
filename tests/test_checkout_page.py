import pytest
from pages.checkout_page import CheckoutPage
from locators.ordercomplite_page_locators import OrderComlitePageLocators
from locators.main_page_locators import MainPageLocators
from utils.data import test_cases_complete
import allure

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

        assert checkout_page.is_order_success_displayed()

        checkout_page.click_status()
        checkout_page.click_scuter()
        assert checkout_page.is_scuter_displayed()

        checkout_page.click_yandex()
        assert checkout_page.is_dzen_in_url()
        