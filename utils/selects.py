from selenium.webdriver.support import expected_conditions as EC
from locators.checkout_page_locators import CheckoutPageLocatorsOne, CheckoutPageLocatorsTwo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class Select:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_metro_station(self, metro):
        Metro_field = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsOne.FIELD_METRO)
        )
        Metro_field.click()
        
        Metro_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{metro}']"))
        )
        Metro_option.click()

    def select_days(self, day):
        Days_field = self.wait.until(
            EC.element_to_be_clickable(CheckoutPageLocatorsTwo.FIELD_DAYS)
        )
        Days_field.click()

        Days_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{day}']"))
        )
        Days_option.click()