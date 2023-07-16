from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_page_url = 'https://qa-scooter.praktikum-services.ru/order'
    ya_page_url = 'dzen.ru'

    scooter_logo_locator = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    ya_logo_locator = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

    name_locator = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    surname_locator = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    address_locator = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    phone_locator = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]

    subway_locator = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    subway_station_locator_template = "//div[@class ='select-search__select']//div[text() = 'value']"

    further_button_locator = [By.XPATH, ".//button[text() = 'Далее']"]

    order_time_locator = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    date_locator_template = ".//div[text()='value']"

    order_period_locator = [By.CLASS_NAME, "Dropdown-placeholder"]
    list_of_periods_locator = [By.CLASS_NAME, 'Dropdown-option']
    order_period_xpath_template = "//div[text() = 'value']"

    comment_locator = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"]

    list_of_colors_locator = [By.XPATH, "//div[@class ='Order_Checkboxes__3lWSI']//label"]
    color_xpath_template = "//label[text() = 'value']/input"
    container_with_color_locator = [By.XPATH, "//div[@class = 'Order_Checkboxes__3lWSI Order_FilledContainer__2MKAk']"]

    order_button = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Заказать']"]
    order_confirmation_header = [By.XPATH, ".//div[text() = 'Хотите оформить заказ?']"]
    order_confirmation_button_yes = [By.XPATH, ".//button[text() = 'Да']"]
    successful_order_header = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']

