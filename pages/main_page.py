from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
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
        self.scroll_to_element(self.question_locators[index])
        self.click(self.question_locators[index])
    
    def get_answer_text(self, index):
        return self.get_text(self.answer_locators[index])
    
    def is_answer_visible(self, index):
        return self.is_displayed(self.answer_locators[index])