from selenium.webdriver.common.by import By

class ActionConfirmationPageLocators:
    #Название уведомления
    NAME = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")

    #Кнопка "Да"
    BUTTON_YES = (By.XPATH, "//button[contains(text(),'Да')]")

    # Кнопка "Нет"
    BUTTON_NO = (By.XPATH, "//button[contains(text(),'Нет')]")