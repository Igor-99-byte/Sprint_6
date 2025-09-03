from selenium.webdriver.common.by import By

class OrderComlitePageLocators:
    #Название уведомления
    NAME = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")

    #Кнопка "Посмотреть статус"
    BUTTON_STATUS = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")