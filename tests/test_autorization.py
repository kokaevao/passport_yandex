import allure

from pages.authorization_page import Authorization_page

@allure.severity(severity_level="CRITICAL")
def test_incorrect_password(get_username_bret, run_driver):
    with allure.step("Тест автризации пользователя с неверным паролем"):
        ap = Authorization_page(run_driver)
        ap.open_authorization_page()
        ap.input_field_login_email(get_username_bret.get('login'))
        ap.click_button_come_in()
        ap.input_field_password(get_username_bret.get('password'))
        ap.click_button_come_in()
        ap.assert_word(ap.get_word_incorrect_password(), "Неверный пароль")
        ap.get_screenshot()


@allure.severity(severity_level="CRITICAL")
def test_login_by_phone(run_driver):
    with allure.step("Тест автризации пользователя по номеру телефона"):
        ap = Authorization_page(run_driver)
        ap.open_authorization_page()
        ap.click_button_phone()
        ap.input_field_phone(9099869118)
        ap.click_button_come_in()
        ap.assert_word(ap.get_word_enter_sms_code(), "Введите код из смс. Мы отправили его на номер +7 909 ***-**-18")
        ap.get_screenshot()


@allure.severity(severity_level="CRITICAL")
def test_login_by_mail(run_driver):
    with allure.step("Тест автризации пользователя с емэйл"):
        ap = Authorization_page(run_driver)
        ap.open_authorization_page()
        ap.input_field_login_email("skvosh1991@mail.ru")
        ap.click_button_come_in()
        ap.input_field_password("Qwerty12345!@#")
        ap.click_button_come_in()
        ap.assert_word(ap.get_word_success_authorization(), "Данные")
        ap.get_screenshot()


@allure.severity(severity_level="CRITICAL")
def test_create_login_myself(run_driver):
    with allure.step("Тест создания аккаунта для себя"):
        ap = Authorization_page(run_driver)
        ap.open_authorization_page()
        ap.click_button_create_id()
        ap.click_button_create_id_myself()
        ap.input_field_phone(9099869118)
        ap.click_button_continue_phone()
        print(ap.get_word_create_account_sms_code())
        ap.assert_word(ap.get_word_create_account_sms_code(), "Подтвердите кодом из смс")
        ap.get_screenshot()


@allure.severity(severity_level="CRITICAL")
def test_forgot_password(run_driver):
    with allure.step("Тест проверка функции забыли пароль"):
        ap = Authorization_page(run_driver)
        ap.open_authorization_page()
        ap.input_field_login_email("skvosh1991")
        ap.click_button_come_in()
        ap.input_field_password("Qwerty")
        ap.click_button_come_in()
        ap.assert_word(ap.get_word_incorrect_password(), "Неверный пароль")
        ap.click_link_not_remember_password()
        ap.assert_word(ap.get_word_enter_captcha(), "Введите символы с картинки")
        ap.get_screenshot()









