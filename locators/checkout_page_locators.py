from selenium.webdriver.common.by import By

#Первая страница
class CheckoutPageLocatorsOne:
    #Поле "Имя"
    FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")

    #Поле "Фамилия"
    FIELD_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")

    #Поле "Адрес: куда привезти заказ"
    FIELD_ADRES= (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    #Поле "Станция метро"
    FIELD_METRO= (By.XPATH, "//input[@placeholder='* Станция метро']")

    #Поле "Телефон: на него позвонит курьер"
    FIELD_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    #Кнопка "Далее"
    BUTTON_NEXT = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

#Вторая страница
class CheckoutPageLocatorsTwo:
    #Поле "Когда привезти самокат"
    FIELD_WHEN = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    #Поле "Срок аренды"
    FIELD_DAYS = (By.XPATH, "//div[@class='Dropdown-placeholder'='* Срок аренды']")

    #Чек-бокс "Черный жемчуг"
    FIELD_BLACK = (By.XPATH, "//input[@id='black']")

    #Чек-бокс "Серая безысходность"
    FIELD_GREY = (By.XPATH, "//input[@id='grey']")

    #Поле "Комментарий для курьера"
    FIELD_COM = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    #Кнопка "Заказать"
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")