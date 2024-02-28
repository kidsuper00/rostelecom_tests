from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from conftest import web_driver
from pages.autn_page import AuthPage, AuthRegistration
import time
from pages.locators import AuthLocators


def test_auth_page(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)
    page.enter_phone("+79117805671")
    page.enter_pass("Yakish98")
    page.btn_click()
    time.sleep(3)


def test_auth_email(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)
    page.enter_email("alexeystag@mail.ru")
    page.enter_pass("Yakish98")
    page.btn_click()
    time.sleep(3)


def test_auth_number(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)
    page.enter_number("2780151855161")
    page.enter_pass("Yakish98")
    page.btn_click()
    time.sleep(3)


def test_password_masking(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(7)

    # локатор маскировки пароля
    password_mask = web_driver.find_element(*AuthLocators.AUTH_PASS_MASK)
    assert password_mask.is_displayed(), "Password masking not visible"

    # После ввода пароля и двойного нажатия на глазик он дважды меняет состояние на отображение пароля
    page.enter_pass("123")
    time.sleep(2)
    password_mask.click()
    time.sleep(2)
    assert password_mask.is_displayed(), "Password is not open"


def test_forgot_password_links(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # "Забыл пароль" и возврат на страницу авторизации
    forgot_password_link = web_driver.find_element(*AuthLocators.AUTH_FORGOT_PASS_LINK)
    forgot_password_link.click()
    time.sleep(3)

    # Вернемся назад
    web_driver.back()
    time.sleep(3)

    # Проверим, что вернулись на страницу авторизации
    assert '/auth' in web_driver.current_url, "Did not return to the login page"


def test_user_agreement_link(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Локатор для ссылки на пользовательское соглашение
    user_agreement_link = web_driver.find_element(*AuthLocators.AUTH_USER_AGREEMENT_LINK)
    user_agreement_link.click()
    time.sleep(5)


def test_help_links(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Локатор для ссылки "Помощь"
    help_link = web_driver.find_element(*AuthLocators.AUTH_HELP_LINK)
    help_link.click()
    time.sleep(3)


def test_registration_link(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Ссылка на регистрацию
    registration_link = web_driver.find_element(*AuthLocators.AUTH_REGISTRATION)
    registration_link.click()
    time.sleep(5)

    # Тут можно добавить проверки для страницы регистрации


def test_copy_hidden_password(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    password_field = web_driver.find_element(*AuthLocators.AUTH_PASS)
    page.enter_pass("Yakish98")
    time.sleep(3)

    # Копируем скрытый пароль
    password_field.send_keys(Keys.CONTROL, 'a')
    password_field.send_keys(Keys.CONTROL, 'c')

    # Вставляем скопированный пароль в другое поле
    another_field = web_driver.find_element(By.CSS_SELECTOR, '#username')
    another_field.send_keys(Keys.CONTROL, 'v')
    time.sleep(5)

    # Проверяем, что скрытый пароль не скопировался
    assert another_field.text != "Yakish98", "Hidden password copied"


# Авторизация через Вконтакте
def test_auth_vk(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    page = web_driver.find_element(*AuthLocators.AUTH_VK)
    page.click()
    time.sleep(3)


# Авторизация через OK
def test_auth_ok(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    page = web_driver.find_element(*AuthLocators.AUTH_OK)
    page.click()
    time.sleep(3)


# Авторизация через Яндекс
def test_auth_ya(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    page = web_driver.find_element(*AuthLocators.AUTH_YANDEX)
    page.click()
    time.sleep(3)


def test_footer_user_agreement_link(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Нажать на ссылку "Пользовательское соглашение" в футере
    btn = web_driver.find_element(*AuthLocators.AUTH_FOOTER_USER_AGREEMENT_LINK)
    btn.click()
    time.sleep(5)


def test_footer_privacy_policy(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Нажать на ссылку "Соглашение с Политикой конфиденциальности" в футере
    btn = web_driver.find_element(*AuthLocators.AUTH_FOOTER_PRIVACY_POLICY)
    btn.click()
    time.sleep(5)


def test_footer_cookie_hint(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Нажать на ссылку "Cookie" в футере
    cookie = web_driver.find_element(*AuthLocators.AUTH_COOKIE)
    cookie.click()
    time.sleep(3)

    # Проверить, что открылась подсказка по использованию Cookie
    assert cookie.is_displayed(), "Cookie hint not displayed"



    # Логотип
# def test_logo_navigation(web_driver):
#     page = AuthPage(web_driver)
#     page.open_auth_page()
#     time.sleep(5)
#
#     page.logo_click()
#     time.sleep(3)


# НЕГАТИВНЫЕ ТЕСТЫ:

# def test_registration_with_existing_data(web_driver):
#     page = AuthPage(web_driver)
#     page.open_auth_page()
#     time.sleep(10)
#
#     # Откроем страницу регистрации
#
#     registration_page = web_driver.find_element(*AuthLocators.AUTH_REGISTRATION)
#     registration_page.click()
#     time.sleep(5)
#
#     # Заполним поля регистрации с данными уже существующего пользователя
#     first_name = "Алексей"
#     last_name = "Яковлев"
#     city = "Санкт-Петербург"
#     email_or_phone = "alexeystag@mail.ru"
#     password = "Yakish98"
#
#     registration_page.enter_first_name(first_name)
#     registration_page.enter_last_name(last_name)
#     registration_page.enter_city(city)
#     registration_page.enter_email_or_phone(email_or_phone)
#     registration_page.enter_pass(password)
#     registration_page.enter_pass_confirm(password)
#     registration_page.click_register_button()
#     time.sleep(3)
#
#     # # Проверим, что мы видим сообщение об ошибке
#     # assert registration_page.is_error_message_displayed(), "Error message not displayed for duplicate registration"


def test_empty_password(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(7)

    # Оставляем поле пароля пустым и пытаемся войти
    empty_password = web_driver.find_element(*AuthLocators.AUTH_PASS)
    empty_password.click()

    page.enter_phone("+79117805671")
    page.enter_pass("")
    page.btn_click()
    time.sleep(5)

    # Проверяем, что отобразилось сообщение об ошибке
    assert empty_password.is_displayed(), "Error message not displayed for empty password"


def test_wrong_password(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(10)

    # Оставляем поле пароля пустым и пытаемся войти
    wrong_password = web_driver.find_element(*AuthLocators.AUTH_PASS)
    wrong_password.click()

    page.enter_phone("+79117805671")
    page.enter_pass("212445")
    page.btn_click()
    time.sleep(5)

    # Проверяем, что отобразилась ошибка в поле ввода
    assert web_driver.find_element(
        *AuthLocators.AUTH_ERROR_LGN).is_displayed(), "Error message displayed for wrong password"


def test_wrong_phone(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Оставляем поле пароля пустым и пытаемся войти
    wrong_password = web_driver.find_element(*AuthLocators.AUTH_PHONE)
    wrong_password.click()

    page.enter_phone("+79123231122")
    page.enter_pass("Yakish98")
    page.btn_click()
    time.sleep(5)

    # Проверяем, что отобразилась ошибка в поле ввода
    assert web_driver.find_element(
        *AuthLocators.AUTH_ERROR_LGN).is_displayed(), "Error message displayed for wrong phone number"


def test_wrong_number(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Оставляем поле пароля пустым и пытаемся войти
    wrong_number = web_driver.find_element(*AuthLocators.AUTH_NUMBER)
    wrong_number.click()

    page.enter_number("278015185543")
    page.enter_pass("Yakish98")
    page.btn_click()
    time.sleep(2)

    # Проверяем, что отобразилось сообщение об ошибке
    assert web_driver.find_element(
        *AuthLocators.AUTH_ERROR_LGN).is_displayed(), "Error message not displayed for wrong number"


def test_wrong_email(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Оставляем поле пароля пустым и пытаемся войти
    wrong_number = web_driver.find_element(*AuthLocators.AUTH_EMAIL)
    wrong_number.click()

    page.enter_number("asdadasd@sdd.asd")
    page.enter_pass("Yakish98")
    page.btn_click()
    time.sleep(2)

    # Проверяем, что отобразилось сообщение об ошибке
    assert web_driver.find_element(
        *AuthLocators.AUTH_ERROR_LGN).is_displayed(), "Error message not displayed for wrong number"
