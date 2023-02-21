import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'
        self.accepting_cookies_button = [By.XPATH, ".//button[text() = 'да все привыкли']"]


    @allure.step('Переходим на стартовую страницу')
    def go_to_base_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator),
                                                      message=f"Element not found {locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(locator),
                                                      message=f"Not find {locator}")

    def set_value_for_element(self, locator, value):
        return self.find_element(locator).send_keys(value)

    def get_value_of_element(self, locator):
        return self.find_element(locator).get_attribute('value')

    def get_text_of_element(self, locator):
        return self.find_element(locator).text

    @allure.step('Соглашаемся принять cookies')
    def accept_cookies(self):
        return self.find_element(self.accepting_cookies_button).click()

    def start_work(self):
        self.go_to_base_page()
        self.accept_cookies()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключаемся на другое окно')
    def switch_windows(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, 5).until_not(EC.url_contains('blank'))
