import allure
from locators_and_data.order_page_locators import OrderPageLocators as OPL
from pages.main_page import MainPageOrder
from pages.order_page import OrderPage


class TestTransitionToOrder:

    @allure.title('Проверка перехода на страницу оформления заказа по кнопке Заказать на хэдере')
    @allure.description('На стартовой странице ищем кнопку Заказать на хэдере, кликаем по ней, проверяем, что страница изменилась на страницу заказа')
    def test_transition_to_order_page_with_header_button_order_page_opened(self, driver):
        main_page = MainPageOrder(driver)
        main_page.start_work()
        main_page.click_header_order_button()
        assert main_page.driver.current_url == OPL.order_page_url

    @allure.title('Проверка перехода на страницу оформления заказа по кнопке Заказать внизу страницу')
    @allure.description('На стартовой странице ищем кнопку Заказать внизу страницы, кликаем по ней, проверяем, что страница изменилась на страницу заказа')
    def test_transition_to_order_page_with_finish_button_order_page_opened(self, driver):
        main_page = MainPageOrder(driver)
        main_page.start_work()
        main_page.scroll_to_finish_order_button()
        main_page.click_finish_order_button()
        assert main_page.driver.current_url == OPL.order_page_url


class TestTransitionFromOrder:

    @allure.title('Проверка перехода на стартовую страницу при клике по логотипу Самоката')
    @allure.description(
        'На странице заказа ищем кнопку с логотипом Самоката, кликаем по ней, проверяем, что страница изменилась на стартовую')
    def test_transition_from_order_page_with_scooter_logo_main_page_opened(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        order_page.click_scooter_logo()
        assert order_page.driver.current_url == order_page.base_url

    @allure.title('Проверка открытия главной страницы Яндекса при клике по логотипу Яндекса')
    @allure.description(
        'На странице заказа ищем кнопку с логотипом Яндекса, кликаем по ней, проверяем, что открылась вторая вкладка со страницей Яндекса')
    def test_transition_from_order_page_with_ya_logo_ya_page_opened(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        order_page.click_ya_logo()
        order_page.switch_windows()
        assert OPL.ya_page_url in order_page.driver.current_url


class TestOrderProcess:

    @allure.title('Проверка заполнения поля Имя')
    @allure.description(
        'На странице заказа ищем поле Имя, заполняем случайным именем и проверяем, что значение поля соответствует введенному')
    def test_order_set_random_name_name_accepted(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        name = order_page.generate_random_name()
        order_page.set_name(name)
        assert order_page.get_value_of_element(OPL.name_locator) == name

    @allure.title('Проверка заполнения поля Фамилия')
    @allure.description(
        'На странице заказа ищем поле Фамилия, заполняем случайной фамилией и проверяем, что значение поля соответствует введенному')
    def test_order_set_random_surname_surname_accepted(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        surname = order_page.generate_random_name()
        order_page.set_surname(surname)
        assert order_page.get_value_of_element(OPL.surname_locator) == surname

    @allure.title('Проверка заполнения поля Адрес')
    @allure.description(
        'На странице заказа ищем поле Адрес, заполняем случайным адресом и проверяем, что значение поля соответствует введенному')
    def test_order_set_random_address_address_accepted(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        address = order_page.generate_random_address()
        order_page.set_address(address)
        assert order_page.get_value_of_element(OPL.address_locator) == address

    @allure.title('Проверка заполнения поля Станция метро')
    @allure.description(
        'На странице заказа ищем поле Станция метро, заполняем случайной станцией и проверяем, что значение поля соответствует введенному')
    def test_order_set_random_subway_subway_accepted(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        station = order_page.choose_random_subway()
        order_page.set_subway(station)
        assert order_page.get_value_of_element(OPL.subway_locator) == station

    @allure.title('Проверка заполнения поля Номер телефона')
    @allure.description(
        'На странице заказа ищем поле Номер телефона, заполняем случайным номером и проверяем, что значение поля соответствует введенному')
    def test_order_set_random_phone_phone_accepted(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        phone = order_page.generate_random_phone()
        order_page.set_phone(phone)
        assert order_page.get_value_of_element(OPL.phone_locator) == phone

    @allure.title('Проверка заполнения поля Время заказа')
    @allure.description(
        'На странице заказа ищем поле Время заказа, заполняем случайной датой и проверяем, что значение поля соответствует введенному')
    def test_order_set_random_order_time_time_accepted(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        order_page.fill_first_page_of_order_with_test_data()
        order_time = order_page.generate_random_order_time()
        order_page.set_order_time(order_time)
        assert order_page.get_value_of_element(OPL.order_time_locator) == order_time

    @allure.title('Проверка выбора Периода заказа')
    @allure.description(
        'На странице заказа ищем поле Период заказа, заполняем случайным периодом и проверяем, что значение поля соответствует введенному')
    def test_order_set_random_order_period_period_accepted(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        order_page.fill_first_page_of_order_with_test_data()
        order_period = order_page.choose_random_order_period()
        order_page.set_order_period(order_period)
        assert order_page.get_text_of_element(OPL.order_period_locator) == order_period

    @allure.title('Проверка выбора цвета')
    @allure.description(
        'На странице заказа ищем поле Цвет, выбираем случайный цвет и проверяем, что значение поля соответствует введенному')
    def test_order_set_random_color_color_accepted(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        order_page.fill_first_page_of_order_with_test_data()
        color = order_page.choose_random_color()
        order_page.set_color(color)
        assert order_page.find_element(OPL.container_with_color_locator)

    @allure.title('Проверка заполнения поля Комментарий')
    @allure.description(
        'На странице заказа ищем поле Комментарий, заполняем случайной фразой и проверяем, что значение поля соответствует введенному')
    def test_order_set_random_comment_comment_accepted(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        order_page.fill_first_page_of_order_with_test_data()
        comment = order_page.generate_random_comment()
        order_page.set_comment(comment)
        assert order_page.get_value_of_element(OPL.comment_locator) == comment

    @allure.title('Проверка успешно размещенного заказа')
    @allure.description(
        'На странице заказа заполняем все обязательные поля, кликаем по кнопке Заказать, подтверждаем заказ и проверяем, что появилось окно с подтверждением')
    def test_full_order_filled_successful_order(self, driver):
        order_page = OrderPage(driver)
        order_page.start_work_with_order()
        order_page.fill_first_page_of_order_with_test_data()
        order_page.fill_second_page_of_order_with_test_data()
        order_page.click_yes_on_confirmation_form()
        assert 'Заказ оформлен' in order_page.get_text_of_element(OPL.successful_order_header)
