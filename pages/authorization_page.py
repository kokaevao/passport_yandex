from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.logger import Logger

from base.base_class import Base


class Authorization_page(Base):

    url = 'https://passport.yandex.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    field_login_email = '//*[@id="passp-field-login"]'
    field_phone = '//*[@id="passp-field-phone"]'
    field_password = '//*[@id="passp-field-passwd"]'
    button_come_in = '//*[@id="passp:sign-in"]'
    button_create_id = '//*[@id="passp:exp-register"]'
    button_create_id_myself = "//button[contains( text(),'Для себя')]"
    button_phone = '//*[@data-type="phone"]'
    button_continue_phone = '//*[@id="passp:phone:controls:next"]'
    link_not_remember_password = '//*[@id="field:link-passwd"]/a'
    word_add_account_yandex = '//*[@class="passp-add-account-page-title"]'
    word_incorrect_password = '//*[@id="field:input-passwd:hint"]'
    word_enter_sms_code = "//div[contains( text(),'Введите код из смс. Мы')]"
    word_create_account_sms_code = "//div[contains( text(),'Подтвердите кодом из')]"
    word_success_authorization = "//a[contains( text(),'Данные')]"
    word_enter_captcha = "//h1[contains( text(),'Введите символы')]"




    # Getters
    def get_field_login_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_login_email)))

    def get_field_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_phone)))

    def get_field_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_password)))

    def get_button_come_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_come_in)))

    def get_button_create_id(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_create_id)))

    def get_button_create_id_myself(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_create_id_myself)))

    def get_button_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_phone)))

    def get_button_continue_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue_phone)))

    def get_link_not_remember_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_not_remember_password)))

    def get_word_add_account_yandex(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_add_account_yandex)))

    def get_word_incorrect_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_incorrect_password)))

    def get_word_enter_sms_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_enter_sms_code)))

    def get_word_create_account_sms_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_create_account_sms_code)))

    def get_word_success_authorization(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_success_authorization)))

    def get_word_enter_captcha(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_enter_captcha)))

    # Actions

    def input_field_login_email(self, login_email):
        self.get_field_login_email().send_keys(login_email)

    def input_field_phone(self, phone):
        self.get_field_phone().send_keys(phone)

    def input_field_password(self, password):
        self.get_field_password().send_keys(password)

    def click_button_come_in(self):
        self.get_button_come_in().click()

    def click_button_create_id(self):
        self.get_button_create_id().click()

    def click_button_create_id_myself(self):
        self.get_button_create_id_myself().click()

    def click_button_phone(self):
        self.get_button_phone().click()

    def click_button_continue_phone(self):
        self.get_button_continue_phone().click()

    def click_link_not_remember_password(self):
        self.get_link_not_remember_password().click()


    # Methods

    def open_authorization_page(self):
        Logger.add_start_step(method='Открытие страницы авторизации')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_word(self.get_word_add_account_yandex(), "Войдите с Яндекс ID")
        Logger.add_end_step(url=self.driver.current_url, method='Открытие страницы авторизации')







