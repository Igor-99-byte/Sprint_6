import pytest
from pages.checkout_page import CheckoutPage
from utils.data import test_cases_complete
import allure

@pytest.mark.usefixtures("browser")
class TestCheckout:
    @pytest.mark.parametrize("name,last_name,adres,metro,phone,when,days,comm", test_cases_complete)
    @allure.story("Проверка успешного оформления заказа")
    @allure.title("Тест оформления заказа с данными")
    def test_checkout_page(self, name, last_name, adres, metro, phone, when, days, comm):
        checkout_page = CheckoutPage(self.driver)

        with allure.step("Нажать кнопку 'Заказать' вверху страницы"):
            checkout_page.click_button_up()
        
        with allure.step("Заполнить первую страницу формы данными"):
            checkout_page.fill_first_page_form(name, last_name, adres, metro, phone)
        
        with allure.step("Нажать кнопку 'Далее'"):
            checkout_page.click_button_next()
        
        with allure.step("Заполнить вторую страницу формы данными"):
            checkout_page.fill_second_page_form(when, days, comm)

        with allure.step("Нажать кнопку 'Заказать'"):
            checkout_page.click_order()
        
        with allure.step("Подтвердить заказ в модальном окне"):
            checkout_page.click_yes()

        with allure.step("Проверить успешное оформление заказа"):
            assert checkout_page.is_order_success_displayed()

        with allure.step("Нажать кнопку 'Статус заказа'"):
            checkout_page.click_status()
        
        with allure.step("Нажать на логотип Самоката"):
            checkout_page.click_scuter()
        
        with allure.step("Проверить отображение главной страницы"):
            assert checkout_page.is_scuter_displayed()

        with allure.step("Нажать на логотип Яндекса"):
            checkout_page.click_yandex()
        
        with allure.step("Проверить переход на страницу Dzen"):
            assert checkout_page.is_dzen_in_url()
        