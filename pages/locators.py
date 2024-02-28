from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthLocators:
    # AUTH_REGISTRATION = None
    AUTH_LOGO = (By.XPATH, '/html/body/div[1]/header/div/div/svg')
    AUTH_EMAIL = (By.CSS_SELECTOR, '#username')
    AUTH_PASS = (By.CSS_SELECTOR, '#password')
    AUTH_BTN = (By.CSS_SELECTOR, '#kc-login')
    AUTH_PHONE = (By.CSS_SELECTOR, '#username')
    AUTH_NUMBER = (By.CSS_SELECTOR, '#username')
    AUTH_PASS_MASK = (By.CSS_SELECTOR, '.rt-eye-icon')
    AUTH_FORGOT_PASS_LINK = (By.CSS_SELECTOR, '#forgot_password')
    AUTH_VK = (By.XPATH, '//*[@id="oidc_vk"]')
    AUTH_OK = (By.CSS_SELECTOR, '#oidc_ok')
    AUTH_YANDEX = (By.CSS_SELECTOR, '#oidc_ya')
    AUTH_USER_AGREEMENT_LINK = (By.XPATH, '/html/body/div[1]/footer/div[1]/div[2]/a/span[2]')
    AUTH_FOOTER_USER_AGREEMENT_LINK = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    AUTH_FOOTER_PRIVACY_POLICY = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    AUTH_COOKIE = (By.CSS_SELECTOR, '#cookies-tip-open')
    AUTH_ERROR_LGN = (By.CSS_SELECTOR, '#form-error-message')

    AUTH_HELP_LINK = (By.CSS_SELECTOR, '#faq-open')
    AUTH_REGISTRATION = (By.XPATH, '//*[@id="kc-register"]')
    AUTH_CITY = (By.XPATH, '//span[contains(@class, "rt-input__mask-start") and contains(text(), "Москва г")]')
    AUTH_FIRST_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    AUTH_LAST_NAME = (By.CSS_SELECTOR, '#lastname')
    AUTH_EMAIL_OR_PHONE = (By.CSS_SELECTOR, '#address"')
    AUTH_REGISTRATION_BTN = (By.CSS_SELECTOR, '#register')
    AUTH_REGISTRATION_PASS = (By.CSS_SELECTOR, '#password')
    AUTH_PASS_CONFIRM = (By.CSS_SELECTOR, '#password-confirm')
