from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.question_locators = [
            MainPageLocators.SELECT_1,
            MainPageLocators.SELECT_2,
            MainPageLocators.SELECT_3,
            MainPageLocators.SELECT_4,
            MainPageLocators.SELECT_5,
            MainPageLocators.SELECT_6,
            MainPageLocators.SELECT_7,
            MainPageLocators.SELECT_8
        ]
        self.answer_locators = [
            MainPageLocators.ELEMENT_1,
            MainPageLocators.ELEMENT_2,
            MainPageLocators.ELEMENT_3,
            MainPageLocators.ELEMENT_4,
            MainPageLocators.ELEMENT_5,
            MainPageLocators.ELEMENT_6,
            MainPageLocators.ELEMENT_7,
            MainPageLocators.ELEMENT_8
        ]
    
    def click_question(self, index):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        element = self.wait.until(
            EC.element_to_be_clickable(self.question_locators[index])
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        element.click()
    
    def get_answer_text(self, index):
        element = self.wait.until(
            EC.visibility_of_element_located(self.answer_locators[index])
        )
        return element.text