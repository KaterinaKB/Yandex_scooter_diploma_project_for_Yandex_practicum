import random
import allure
from selenium.webdriver.common.by import By
from locators_and_data.order_page_locators import OrderPageLocators as OPL
from locators_and_data import order_page_data as OPD
from pages.base_page import BasePage
import datetime
now = datetime.datetime.now()


class OrderPage(BasePage):

    @allure.step('Переходим на страницу формирования заказа')
    def go_to_order_page(self):
        return self.driver.get(OPL.order_page_url)

    def start_work_with_order(self):
        self.go_to_order_page()
        self.accept_cookies()

    @allure.step('Кликаем по логотипу Самоката')
    def click_scooter_logo(self):
        return self.find_element(OPL.scooter_logo_locator).click()

    @allure.step('Кликаем по логотипу Яндекса')
    def click_ya_logo(self):
        return self.find_element(OPL.ya_logo_locator).click()

    @allure.step('Генерируем случайное Имя')
    def generate_random_name(self):
        name = OPD.generate_random_data('name')
        return name

    @allure.step('Заполняем поле Имя')
    def set_name(self, name):
        return self.set_value_for_element(OPL.name_locator, name)

    @allure.step('Генерируем случайную Фамилию')
    def generate_random_surname(self):
        surname = OPD.generate_random_data('surname')
        return surname

    @allure.step('Заполняем поле Фамилия')
    def set_surname(self, surname):
        return self.set_value_for_element(OPL.surname_locator, surname)

    @allure.step('Генерируем случайный Адрес')
    def generate_random_address(self):
        address = OPD.generate_random_data('address')
        return address

    @allure.step('Заполняем поле Адрес')
    def set_address(self, address):
        return self.set_value_for_element(OPL.address_locator, address)

    @allure.step('Выбираем случайную станцию метро')
    def choose_random_subway(self):
        random_station = random.choice(OPD.list_of_subway_stations)
        return random_station

    @allure.step('Заполняем поле Стация метро')
    def set_subway(self, station):
        self.find_element(OPL.subway_locator).click()
        station_locator = [By.XPATH, OPL.subway_station_locator_template.replace('value', station)]
        return self.find_element(station_locator).click()

    @allure.step('Генерируем случайный Номер телефона')
    def generate_random_phone(self):
        phone = OPD.generate_random_data('phone')
        return phone

    @allure.step('Заполняем поле Номер телефона')
    def set_phone(self, phone):
        return self.set_value_for_element(OPL.phone_locator, phone)

    @allure.step('Кликаем по кнопке Далее')
    def click_further_button(self):
        return self.find_element(OPL.further_button_locator).click()

    @allure.step('Заполняем первую страницу данных для заказа')
    def fill_first_page_of_order_with_test_data(self):
        self.set_name(OPD.test_data_for_order['name'])
        self.set_surname(OPD.test_data_for_order['surname'])
        self.set_address(OPD.test_data_for_order['address'])
        self.set_subway(OPD.test_data_for_order['subway'])
        self.set_phone(OPD.test_data_for_order['phone'])
        self.click_further_button()

    @allure.step('Выбираем следующий день из календаря')
    def choose_next_day_from_calendar(self):
        self.find_element(OPL.order_time_locator).click()
        date = str(now.day + 1)
        date_locator = [By.XPATH, OPL.date_locator_template.replace('value', date)]
        self.find_element(date_locator).click()

    @allure.step('Генерируем случайную Дату')
    def generate_random_order_time(self):
        order_time = OPD.generate_random_data('order_time')
        return order_time

    @allure.step('Заполняем поле Время заказа')
    def set_order_time(self, order_time):
        return self.set_value_for_element(OPL.order_time_locator, order_time)

    @allure.step('Выбираем случайный Период заказа')
    def choose_random_order_period(self):
        self.find_element(OPL.order_period_locator).click()
        list_of_period_elements = self.find_elements(OPL.list_of_periods_locator)
        list_of_periods = [i.text for i in list_of_period_elements]
        random_period = random.choice(list_of_periods)
        self.find_element(OPL.order_period_locator).click()
        return random_period

    @allure.step('Заполняем поле Период заказа')
    def set_order_period(self, period):
        self.find_element(OPL.order_period_locator).click()
        period_xpath = OPL.order_period_xpath_template.replace('value', period)
        period_locator = [By.XPATH, period_xpath]
        return self.find_element(period_locator).click()

    @allure.step('Выбираем случайный Цвет самоката')
    def choose_random_color(self):
        list_of_color_elements = self.find_elements(OPL.list_of_colors_locator)
        list_of_colors = [i.text for i in list_of_color_elements]
        random_color = random.choice(list_of_colors)
        return random_color

    @allure.step('Активируем чекбокс с Цветом')
    def set_color(self, color):
        color_xpath = OPL.color_xpath_template.replace('value', color)
        color_locator = [By.XPATH, color_xpath]
        return self.find_element(color_locator).click()

    @allure.step('Генерируем случайный комментарий')
    def generate_random_comment(self):
        comment = OPD.generate_random_data('comment')
        return comment

    @allure.step('Заполняем поле комментарий')
    def set_comment(self, comment):
        return self.set_value_for_element(OPL.comment_locator, comment)

    @allure.step('Кликаем по кнопке Заказать')
    def click_order_button(self):
        return self.find_element(OPL.order_button).click()

    @allure.step('Заполняем вторую страницу данных для заказа')
    def fill_second_page_of_order_with_test_data(self):
        self.choose_next_day_from_calendar()
        self.set_order_period(OPD.test_data_for_order['period'])
        self.set_color(OPD.test_data_for_order['color'])
        self.click_order_button()

    @allure.step('Кликаем по кнопке Да в форме подтверждения заказа')
    def click_yes_on_confirmation_form(self):
        return self.find_element(OPL.order_confirmation_button_yes).click()
