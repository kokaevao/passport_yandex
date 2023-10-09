import pytest


from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from lib.my_requests import MyRequests

"""Функция получения пользователя Bret"""
@pytest.fixture
def get_username_bret():
    response = MyRequests.get("/users")
    login = response.json()[0]['username']
    email = response.json()[0]['email']
    phone = response.json()[0]['phone']
    password = response.json()[0]['website']
    result = {'login': login, 'email': email, 'phone': phone, 'password': password}
    return result


"""Функция запуска и закрытия драйвера"""
@pytest.fixture
def run_driver():
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    options = webdriver.ChromeOptions()
    options.set_capability("loggingPrefs", {'performance': 'ALL'})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\akokaev\\Desktop\\Learn_Python\\passport_yandex\\chromedriver.exe')
    driver = webdriver.Chrome(desired_capabilities=caps, options=options, service=g)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    yield driver
    driver.close()



