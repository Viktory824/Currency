from selenium.webdriver.common.by import By


class CurrencyLocators:

    @staticmethod
    def value_from(value):
        return (
            By.XPATH,
            "//select[@name='converterFrom']/ancestor::div[@class='rates-aside__filter-block-line-right']//"
            "div[@class='visible']/span[contains(text(),'{0}')]".format(value))

    @staticmethod
    def value_to(value):
        return (By.XPATH, "//select[@name='converterTo']/ancestor::div[@class='rates-aside__filter-block-line']//"
                          "div[@class='visible']/span[contains(text(),'{0}')]".format(value))

    currency_count_input = (By.XPATH, "//div[@class='rates-aside__filter-block-line-right input']/form/input")

    convert_from_dropdown = (
        By.XPATH, "//div[@class='rates-aside__filter-block-line rates-aside__filter-block-line_field_converter-from']"
                  "//*[@class='select']")

    convert_to_dropdown = (By.XPATH, "//div[@class='rates-aside__filter-block-line']//*[@class='select']")

    convert_button = (By.XPATH, "//button[@class='rates-button']")

    convert_result_inital_value = (By.XPATH, "//span[@class='rates-converter-result__total-from']")

    convert_result_currency_to_name = (By.XPATH, "//span[@class='rates-converter-result__total-to']")

    convert_result_value = (By.XPATH, "//div[@class='rates-converter-result__total']//"
                                      "span[@class='rates-converter-result__total-to']")

    current_value_dropdown_to = (By.XPATH,
                                 "//select[@name='converterTo']/ancestor::div[@class='rates-aside__filter-block-line']"
                                 "//div[@class='select']/header/strong")

    current_value_dropdown_from = (By.XPATH,
                                   "//select[@name='converterFrom']"
                                   "/ancestor::div[@class='rates-aside__filter-block-line-right']"
                                   "//div[@class='select']/header/strong")

    currency_from_with_rub = (By.XPATH, "//table[@class='rates-current__table']//"
                                        "tr[@class='rates-current__table-row rates-current__table-row_odd']/"
                                        "td[@class='rates-current__table-cell rates-current__table-cell_column_name']")

    currency_to_with_rub = (By.XPATH, "//table[@class='rates-current__table']//tr[@class='rates-current__table-row']"
                                      "/td[@class='rates-current__table-cell rates-current__table-cell_column_name']")
