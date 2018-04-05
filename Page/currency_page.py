import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page.currency_locators import CurrencyLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class CurrencyPage(BasePage):
    def __init__(self, driver, currency_value, value_from, value_to):
        super().__init__(driver)
        self.currency_value = currency_value
        self.value_from = value_from
        self.value_to = value_to

    def enter_value_to_count_field(self):
        self.driver.driver.find_element(*CurrencyLocators.currency_count_input).clear()
        self.driver.driver.find_element(*CurrencyLocators.currency_count_input).send_keys(self.currency_value)

    def select_value_convert_from_dropdown(self):
        self.driver.driver.find_element(*CurrencyLocators.convert_from_dropdown).click()
        element = CurrencyLocators.value_from(self.value_from)
        self.scroll_to_element()
        self.driver.driver.find_element(*element).click()

    def select_value_convert_to_dropdown(self):
        self.driver.driver.find_element(*CurrencyLocators.convert_to_dropdown).click()
        element = CurrencyLocators.value_to(self.value_to)
        self.driver.driver.find_element(*element).click()

    def scroll_to_element(self, fix_element=250):
        self.driver.driver.execute_script("window.scrollTo(0, {0});".format(fix_element))

    def scroll_to_page_end(self):
        self.driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_to_convert_button(self):
        self.driver.driver.find_element(*CurrencyLocators.convert_button).click()

    def convert_result_init_value_and_currency(self):
        convert_result_init_val = WebDriverWait(self.driver.driver, 10).until(
            EC.visibility_of_element_located(CurrencyLocators.convert_result_inital_value))

        if convert_result_init_val:
            convert_result_init_val = self.driver.driver.find_element(
                *CurrencyLocators.convert_result_inital_value).text
        return str(convert_result_init_val.replace(' ', '')).split(',')

    def get_convert_result_init_value(self):
        return int(self.convert_result_init_value_and_currency()[0].replace(',', '.'))

    def get_convert_result_currency_name(self):
        val = self.convert_result_init_value_and_currency()[1]
        list_of_val = re.findall(r'[A-Za-z]{3}', val)
        return list_of_val[0]

    def check_result_currency_inital_value(self):
        return int(self.get_convert_result_init_value()) == self.currency_value

    def check_result_currency_from_name(self):
        return self.get_convert_result_currency_name() == self.value_from

    def check_result_currency_to_name(self):
        convert_result_currency_to_name = \
            self.driver.driver.find_element(*CurrencyLocators.convert_result_currency_to_name).text
        result_currency_to_name = re.findall(r'[A-Za-z]{3}', convert_result_currency_to_name)[0]
        return result_currency_to_name == self.value_to

    def get_current_value_from_dropdown_to(self):
        return self.driver.driver.find_element(*CurrencyLocators.current_value_dropdown_to).text

    def get_current_value_from_dropdown_from(self):
        return self.driver.driver.find_element(*CurrencyLocators.current_value_dropdown_from).text

    def check_value_from_convert(self):
        currency_from_name = str(self.driver.driver.find_element(*CurrencyLocators.currency_from_with_rub).text).split(
            '/')[0]
        return self.value_from == re.sub(' ', '', currency_from_name)

    def check_value_to_convert(self):
        currency_to_name = str(self.driver.driver.find_element(*CurrencyLocators.currency_to_with_rub).text).split('/')[
            0]
        return self.value_to == re.sub(' ', '', currency_to_name)
