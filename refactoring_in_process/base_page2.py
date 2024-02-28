from urllib.parse import urlparse
from refactoring_in_process.locators2 import AuthLocators
import time

class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def open_page(self, url):
        self.driver.get(url)

    def back(self):
        pass

    def enter_email_phone_number(self, value):
        username = self.driver.find_element(*AuthLocators.AUTH_EMAIL_PHONE_NUMBER)
        username.send_keys(value)

    def btn_click(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_BTN)
        btn.click()
        time.sleep(3)

