import allure
import pytest
from locators_and_data import main_page_data as MPD
from pages.main_page import MainPageFAQ


class TestFAQ:

    @allure.title('Проверка корректности ответа на вопрос')
    @allure.description('На стартовой старнице ищем вопрос, кликаем по нему и сверяем полученный ответ с ожидаемым')
    @pytest.mark.parametrize('faq', list(MPD.dict_of_answers))
    def test_faq_open_question_right_answer_shown(self, driver, faq):
        faq_page = MainPageFAQ(driver)
        faq_page.start_work_with_faq()
        question = faq
        right_answer = MPD.dict_of_answers[question]
        faq_page.open_question(question)
        answer = faq_page.get_answer(question)
        assert answer == right_answer
