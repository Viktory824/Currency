import os
from selenium import webdriver


class DriverActions:
    def set_up(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--start-maximized')
        browser_path = os.path.realpath('../_webdriver/chromedriver.exe')
        self.driver = webdriver.Chrome(browser_path, chrome_options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.sberbank.ru/ru/quotes/converter")

    def tear_down(self):
        self.driver.quit()
