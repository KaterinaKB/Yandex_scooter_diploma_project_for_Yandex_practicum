from selenium.webdriver.common.by import By


class MainPageLocators:

    header_order_button = [By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"]
    finish_order_button = [By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']/button[text() = 'Заказать']"]
    faq_header_locator = [By.XPATH, ".//div[text() = 'Вопросы о важном']"]
    question_xpath_template = ".//div[text() = 'template']"
    answer_xpath_template = ".//div[text() = 'template']/parent::div/following-sibling::div/p"
