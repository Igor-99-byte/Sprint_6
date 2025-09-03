from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from locators.actionconfirmation_page_locators import ActionConfirmationPageLocators
from locators.ordercomplite_page_locators import OrderComlitePageLocators
from locators.base_page_locators import BasePageLocators
from locators.checkout_page_locators import CheckoutPageLocatorsOne, CheckoutPageLocatorsTwo
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_button_up(self):
        element = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.BATTON_UP)
        )
        element.click()

    def fill_name(self, name):
        Name = self.wait.until(
        EC.element_to_be_clickable(CheckoutPageLocatorsOne.FIELD_NAME)
        )
        Name.send_keys(name)

    def fill_last_name(self, last_name):
        Last_name = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsOne.FIELD_LAST_NAME)
        )
        Last_name.send_keys(last_name)

    def fill_adres(self, adres):
        Adres = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsOne.FIELD_ADRES)
        )
        Adres.send_keys(adres)

    def fill_metro(self, metro):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsOne.FIELD_METRO)
        )
        dropdown.click()
        
        options_list = self.wait.until(
            EC.presence_of_element_located(CheckoutPageLocatorsOne.FIELD_METRO)
        )
        
        desired_option = options_list.find_element(By.XPATH, f"//button[@value={metro}]")
        desired_option.click()

    def fill_phone(self, phone):
        Phone = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsOne.FIELD_PHONE)
        )
        Phone.send_keys(phone)

    def fill_first_page_form(self, name, last_name, adres, metro, phone):
        self.fill_name(name)
        self.fill_last_name(last_name)
        self.fill_adres(adres)
        self.fill_metro(metro)
        self.fill_phone(phone)

    def click_button_next(self):
        Button_next = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsOne.BUTTON_NEXT)
        )
        Button_next.click()

    def fill_when(self, when):
        calendar_field = self.wait.until(
        EC.element_to_be_clickable(CheckoutPageLocatorsTwo.FIELD_WHEN)
    )
        calendar_field.click()
        
        day_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='Choose {when}']"))
        )
        day_element.click()

    def fill_days(self, days):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsTwo.FIELD_DAYS)
        )
        dropdown.click()
        
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@class='Dropdown-menu']//div[{days}]"))
        )
        option.click()

    def fill_colour(self):
        Colour = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsTwo.FIELD_BLACK)
        )
        Colour.click()
    
    def fill_com(self, comm):
        Comm = self.wait.until(
        EC.element_to_be_clickable(CheckoutPageLocatorsTwo.FIELD_COM)
        )
        Comm.send_keys(comm)

    def fill_second_page_form(self, when, days, comm):
        self.fill_when(when)
        self.fill_days(days)
        self.fill_colour()
        self.fill_com(comm)

    def click_order(self):
        Button_order = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsTwo.BUTTON_ORDER)
        )
        Button_order.click()

    def click_yes(self):
        Yes = self.wait.until(
            EC.element_to_be_clickable(ActionConfirmationPageLocators.BUTTON_YES)
        )
        Yes.click()

    def click_status(self):
        status = self.wait.until(
            EC.element_to_be_clickable(OrderComlitePageLocators.BUTTON_STATUS)
        )
        status.click()

    def click_scuter(self):
        scuter = self.wait.until(
            EC.element_to_be_clickable(BasePageLocators.BUTTON_SCOOTER)
        )
        scuter.click()

    def click_yandex(self):
        yandex = self.wait.until(
            EC.element_to_be_clickable(BasePageLocators.BUTTON_YANDEX)
        )
        yandex.click()
