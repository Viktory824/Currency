import allure
import pytest
from conftest import *
from Page.currency_page import CurrencyPage


# @pytest.fixture(autouse=True)
def get_currency_values():
    with open(os.path.abspath('../positive_values.csv')) as csvfile:
        rows = csv.reader(csvfile)
        currency_array = []
        for item in rows:
            currency_array.append(int(item[0]))
        return currency_array


# @pytest.fixture(autouse=True)
def get_currency_names():
    with open(os.path.abspath('../currencies.csv')) as csvfile:
        currency_values_array = []
        rows = csv.reader(csvfile)
        for item in rows:
            currency_values_array.append(item[0])
        return currency_values_array


class Test1:
    currency_name_from = get_currency_names()
    currency_value = get_currency_values()
    currency_name_to = currency_name_from

    @allure.testcase('Положительный сценарий проверки конвертации')
    @pytest.mark.parametrize("currency_from", currency_name_from)
    @pytest.mark.parametrize("currency_value", currency_value)
    @pytest.mark.parametrize("currency_to", currency_name_to)
    def test_converter_currency(self, driver_manager, currency_from='EUR', currency_value=1, currency_to='CHF'):

        if currency_from == currency_to:
            pytest.skip()

        converter = CurrencyPage(driver_manager,
                                 currency_value,
                                 currency_from,
                                 currency_to)
        with allure.step('Step_1: В поле ввода денежных единиц ввести размер конвертируемов валюты'):
            converter.enter_value_to_count_field()
        with allure.step('Step_2: Выбрать из списка название валюты, из которой будет происходить конвертация'):
            converter.select_value_convert_from_dropdown()
        with allure.step('Step_3: Выбрать из списка название валюты, в которую будет происходить конвертация'):
            converter.select_value_convert_to_dropdown()
        with allure.step('Step_4: Нажать на кнопку \'Вы получите\' '):
            converter.scroll_to_element()
            converter.click_to_convert_button()
        with allure.step('Step_5: В блоке \'Вы получите\' размер конвертируемой валюты совпадает с заданным'):
            assert converter.check_result_currency_inital_value()
        with allure.step('Step_6: В блоке \'Вы получите\' название конвертируемой валюты совпадает с заданным'):
            assert converter.check_result_currency_from_name()
        with allure.step('Step_7: В блоке \'Вы получите\' название сконвертированной валюты совпадает с заданным'):
            assert converter.check_result_currency_to_name()

    @allure.testcase('Проверка ввода одинаковых названий валют')
    @pytest.mark.parametrize("currency_from", currency_name_from)
    def test_check_change_currency(self, driver_manager, currency_from='EUR', currency_value=1):

        converter = CurrencyPage(driver_manager,
                                 currency_value,
                                 currency_from,
                                 currency_from)
        with allure.step('Step_1: Выбрать из списка "из" название валюты, из которой планируется конвертация'):
            converter.select_value_convert_from_dropdown()
            inital_value_to_value = converter.get_current_value_from_dropdown_to()
        with allure.step('Step_2: В списке "в" выбрать значение, из шага 1 '):
            converter.scroll_to_element()
            converter.select_value_convert_to_dropdown()
        with allure.step('Step_3: Значение в списке "в" совпадает с первоначальным значением списка "из"'):
            assert converter.get_current_value_from_dropdown_to() == converter.value_from
        with allure.step('Step_4: Значение в  списке "из" совпадает с первоначальным значением списка "в"'):
            assert converter.get_current_value_from_dropdown_from() == inital_value_to_value

    @allure.testcase('Перевод из одной иностранной валюты в другую')
    def test_check_foreign_currency(self, driver_manager, currency_from='EUR', currency_value=1, currency_to='CHF'):

        if currency_from == 'RUB' or currency_to == 'RUB':
            pytest.skip()

        converter = CurrencyPage(driver_manager,
                                 currency_value,
                                 currency_from,
                                 currency_to)
        with allure.step('Step_1: Выбрать из списка "из" название валюты, из которой планируется конвертация'):
            converter.select_value_convert_from_dropdown()
        with allure.step('Step_2: Выбрать из списка "в" название валюты, в которую планируется конвертация '):
            converter.select_value_convert_to_dropdown()
        with allure.step('Step_3: В блоке валют показан курс валюты из ш.1 по отношению RUB'):
            assert converter.check_value_from_convert()
        with allure.step('Step_4:В блоке валют показан курс валюты из ш.2 по отношению RUB'):
            assert converter.check_value_to_convert()
