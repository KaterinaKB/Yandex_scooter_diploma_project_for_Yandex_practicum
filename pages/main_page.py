import allure
from selenium.webdriver.common.by import By
from locators_and_data.main_page_locators import MainPageLocators as MPL
from pages.base_page import BasePage


class MainPageOrder(BasePage):

    @allure.step('Кликаем по кнопке Заказать на хэдере страницы')
    def click_header_order_button(self):
        return self.find_element(MPL.header_order_button).click()

    @allure.step('Кликаем по кнопке Заказать внизу страницы')
    def click_finish_order_button(self):
        return self.find_element(MPL.finish_order_button).click()

    @allure.step('Прокручиваем страницу к кнопке Заказать внизу страницы')
    def scroll_to_finish_order_button(self):
        return self.scroll_to_element(MPL.finish_order_button)


class MainPageFAQ(BasePage):

    @allure.step('Прокручиваем страницу к Важным вопросам')
    def scroll_to_faq(self):
        return self.scroll_to_element(MPL.faq_header_locator)

    def start_work_with_faq(self):
        self.go_to_base_page()
        self.accept_cookies()
        self.scroll_to_faq()

    def create_question_locator(self, question):
        question_xpath = MPL.question_xpath_template.replace('template', question)
        question_locator = [By.XPATH, question_xpath]
        return question_locator

    @allure.step('Кликаем по вопросу, чтобы открыть ответ')
    def open_question(self, question):
        question_locator = self.create_question_locator(question)
        return self.find_element(question_locator).click()

    def create_answer_locator(self, question):
        answer_xpath = MPL.answer_xpath_template.replace('template', question)
        answer_locator = [By.XPATH, answer_xpath]
        return answer_locator

    @allure.step('Получаем ответ')
    def get_answer(self, question):
        answer_locator = self.create_answer_locator(question)
        return self.get_text_of_element(answer_locator)

