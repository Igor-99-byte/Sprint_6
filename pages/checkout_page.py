from pages.base_page import BasePage
from locators.checkout_page_locators import CheckoutPageLocatorsOne, CheckoutPageLocatorsTwo
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from locators.actionconfirmation_page_locators import ActionConfirmationPageLocators
from locators.base_page_locators import BasePageLocators
from locators.ordercomplite_page_locators import OrderComlitePageLocators

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def click_button_up(self):
        self.click(MainPageLocators.BATTON_UP)
    
    def fill_name(self, name):
        self.type_text(CheckoutPageLocatorsOne.FIELD_NAME, name)
    
    def fill_last_name(self, last_name):
        self.type_text(CheckoutPageLocatorsOne.FIELD_LAST_NAME, last_name)
    
    def fill_adres(self, adres):
        self.type_text(CheckoutPageLocatorsOne.FIELD_ADRES, adres)
    
    def fill_metro(self, metro):
        self.click(CheckoutPageLocatorsOne.FIELD_METRO)
        metro_option = (By.XPATH, f"//button[@value='{metro}']")
        self.click(metro_option)
    
    def fill_phone(self, phone):
        self.type_text(CheckoutPageLocatorsOne.FIELD_PHONE, phone)
    
    def fill_first_page_form(self, name, last_name, adres, metro, phone):
        self.fill_name(name)
        self.fill_last_name(last_name)
        self.fill_adres(adres)
        self.fill_metro(metro)
        self.fill_phone(phone)
        self.click_button_next()
    
    def click_button_next(self):
        self.click(CheckoutPageLocatorsOne.BUTTON_NEXT)
    
    def fill_when(self, when):
        self.click(CheckoutPageLocatorsTwo.FIELD_WHEN)
        
        day_locator = (By.XPATH, f"//div[@aria-label='Choose {when}']")
        self.click(day_locator)
    
    def fill_days(self, days):
        self.click(CheckoutPageLocatorsTwo.FIELD_DAYS)
        
        option_locator = (By.XPATH, f"//div[@class='Dropdown-menu']//div[{days}]")
        self.click(option_locator)
    
    def fill_colour(self):
        self.click(CheckoutPageLocatorsTwo.FIELD_BLACK)
    
    def fill_com(self, comm):
        self.type_text(CheckoutPageLocatorsTwo.FIELD_COM, comm)
    
    def fill_second_page_form(self, when, days, comm):
        self.fill_when(when)
        self.fill_days(days)
        self.fill_colour()
        self.fill_com(comm)
        self.click_order()
    
    def click_order(self):
        self.click(CheckoutPageLocatorsTwo.BUTTON_ORDER)
    
    def click_yes(self):
        self.click(ActionConfirmationPageLocators.BUTTON_YES)
    
    def click_status(self):
        self.click(OrderComlitePageLocators.BUTTON_STATUS)
    
    def click_scuter(self):
        self.click(BasePageLocators.BUTTON_SCOOTER)
    
    def click_yandex(self):
        self.click(BasePageLocators.BUTTON_YANDEX)

    def is_order_success_displayed(self):
        success_element = self.wait.until(
            EC.visibility_of_element_located(OrderComlitePageLocators.NAME)
        )
        return "Заказ оформлен" in success_element.text
    
    def is_scuter_displayed(self):
        return self.driver.find_element(MainPageLocators.SCUTER).is_displayed()
    
    def is_dzen_in_url(self):
        return "dzen" in self.driver.current_url