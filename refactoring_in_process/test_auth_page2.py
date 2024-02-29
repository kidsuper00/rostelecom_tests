from selenium.webdriver import Keys
from refactoring_in_process.autn_page2 import AuthPage, AuthRegistration
import time
from refactoring_in_process.locators2 import AuthLocators


def base_test_auth_page(web_driver, username, password="Yakish98"):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)
    if not username.startswith("+"):
        page = web_driver.find_element(AuthLocators.BUTTON_LC_NUMBER).click()
    page.enter_email_phone_number(username)
    page.enter_pass(password)
    page.btn_click()
    time.sleep(5)


def test_auth_phone(web_driver):
    phone = "+79117805671"
    base_test_auth_page(web_driver, username=phone)


def test_auth_email(web_driver):
    email = "alexeystag@mail.ru"
    base_test_auth_page(web_driver, username=email)


def test_auth_number(web_driver):
    number = "2780151855161"
    base_test_auth_page(web_driver, username=number)


def base_test_auth_links(web_driver, *locator):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # "Забыл пароль" и возврат на страницу авторизации
    # base_redirect_link -> forgot_password_link или user_agreement_link или help_link или registration_link
    link = web_driver.find_element(*locator)
    link.click()
    time.sleep(1)


def test_user_agreement_link(web_driver):
    base_test_auth_links(*AuthLocators.AUTH_USER_AGREEMENT_LINK)


def test_help_links(web_driver):
    base_test_auth_links(*AuthLocators.AUTH_HELP_LINK)


def test_registration_link(web_driver):
    base_test_auth_links(*AuthLocators.AUTH_REGISTRATION)


def test_forgot_password_links(web_driver):
    base_test_auth_links(*AuthLocators.AUTH_FORGOT_PASS_LINK)

    # Вернемся назад
    web_driver.back()
    time.sleep(3)

    # Проверим, что вернулись на страницу авторизации
    assert '/auth' in web_driver.current_url, "Did not return to the login page"


def test_password_masking(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # локатор маскировки пароля
    password_mask = web_driver.find_element(*AuthLocators.AUTH_PASS_MASK)
    assert password_mask.is_displayed(), "Password masking not visible"

    # После ввода пароля и двойного нажатия на глазик он дважды меняет состояние на отображение пароля
    page.enter_pass("123")
    time.sleep(2)
    password_mask.click()
    time.sleep(2)
    assert password_mask.is_displayed(), "Password is not open"

    # Тут можно добавить проверки для страницы регистрации


# Негативные тесты:

def test_registration_with_existing_data(web_driver):
    page = AuthRegistration(web_driver)
    # Откроем страницу регистрации
    page = page.open_registration_page()
    time.sleep(5)

    # Заполним поля регистрации с данными уже существующего пользователя
    first_name = "Алексей"
    last_name = "Яковлев"
    city = "Санкт-Петербург"
    phone_or_email = "alexeystag@mail.ru"
    password = "Yakish98"

    page.enter_first_name(first_name)
    page.enter_last_name(last_name)
    page.enter_city(city)
    page.enter_email_or_phone(phone_or_email)
    page.enter_pass(password)
    page.enter_pass_confirm(password)
    page.click_register_button()
    time.sleep(3)
    # Проверим, что мы видим сообщение об ошибке
    assert page.is_error_message_displayed(), "Error message not displayed for duplicate registration"

    # Проверим, что мы видим сообщение об ошибке
    assert page.is_error_message_displayed(), "Error message not displayed for duplicate registration"


def base_test_wrong_auth_data(web_driver, locator, username, password):
    page = AuthPage(web_driver)
    page.open_auth_page()
    time.sleep(5)

    # Оставляем поле пароля пустым и пытаемся войти
    empty_password = web_driver.find_element(locator)
    empty_password.click()

    page.enter_phone(username)
    page.enter_pass(password)
    page.btn_click()
    time.sleep(2)


def test_empty_password(web_driver):
    phone = "+79117805671"
    password = ""
    base_test_wrong_auth_data(web_driver, *AuthLocators.AUTH_PASS, phone, password)

    # Проверяем, что отобразилось сообщение об ошибке
    assert web_driver.find_element(*AuthLocators.AUTH_PASS).is_displayed(), ("Error message not displayed for empty "
                                                                             "password")


def test_wrong_password(web_driver):
    phone = "+79117805671"
    password = "212445"
    base_test_wrong_auth_data(web_driver, *AuthLocators.AUTH_PASS, phone, password)

    # Проверяем, что отобразилась ошибка в поле ввода
    assert web_driver.find_element(*AuthLocators.AUTH_ERROR_LGN).is_displayed(), ("Error message displayed for wrong "
                                                                                  "password")


def test_wrong_phone(web_driver):
    phone = "+791232311"
    password = "Yakish98"
    base_test_wrong_auth_data(web_driver, *AuthLocators.AUTH_EMAIL_OR_PHONE, phone, password)

    # Проверяем, что отобразилась ошибка в поле ввода
    assert web_driver.find_element(*AuthLocators.AUTH_ERROR_LGN).is_displayed(), ("Error message displayed for wrong "
                                                                                  "phone number")


def test_wrong_number(web_driver):
    phone = "278015185543"
    password = "Yakish98"
    base_test_wrong_auth_data(web_driver, *AuthLocators.AUTH_EMAIL_OR_PHONE, phone, password)

    # Проверяем, что отобразилась ошибка в поле ввода
    assert web_driver.find_element(*AuthLocators.AUTH_ERROR_LGN).is_displayed(), ("Error message displayed for wrong "
                                                                                  "phone number")


def test_wrong_email(web_driver):
    number = "asdadasd@sdd.asd"
    password = "Yakish98"
    base_test_wrong_auth_data(web_driver, *AuthLocators.AUTH_EMAIL_OR_PHONE, number, password)

    # Проверяем, что отобразилось сообщение об ошибке
    assert web_driver.find_element(*AuthLocators.AUTH_ERROR_LGN).is_displayed(), ("Error message not displayed for "
                                                                                  "wrong number")


# def test_copy_hidden_password(web_driver):
#     page = AuthPage(web_driver)
#     page.open_auth_page()
#     time.sleep(5)
#
#     password_field = web_driver.find_element(*AuthLocators.AUTH_PASS)
#     page.enter_pass("Yakish98")
#
#     password_mask = web_driver.find_element(*AuthLocators.AUTH_PASS_MASK)
#     assert password_mask.is_displayed(), "Password masking not working"
#
#     # Копируем скрытый пароль
#     password_field.send_keys(Keys.CONTROL, 'a')
#     password_field.send_keys(Keys.CONTROL, 'c')
#
#     # Вставляем скопированный пароль в другое поле
#     another_field = web_driver.find_element(By.CSS_SELECTOR, 'your_another_field_locator')
#     another_field.send_keys(Keys.CONTROL, 'v')
#
#     # Проверяем, что скрытый пароль не скопировался
#     assert another_field.get_attribute("value") == "", "Hidden password copied"
