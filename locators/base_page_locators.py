from selenium.webdriver.common.by import By

class BasePageLocators:
    #Кнопка "Яндекс"
    BUTTON_YANDEX = (By.XPATH, "//img[@alt='Yandex']")

    #Кнопка "Самокат"
    BUTTON_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")