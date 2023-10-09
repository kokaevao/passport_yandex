import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url



    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result



    """Method assert url"""

    def asset_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result


    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\akokaev\\Desktop\\Learn_Python\\passport_yandex\\screen\\' + name_screenshot)