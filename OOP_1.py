from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Test:
    """общий класс, который будет содержать метод для работы в данном тесте"""
    def __init__(self, url='https://www.saucedemo.com/'):
        self.driver = None

    def setup_options(self):
        """настройка опций браузера"""
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return options

    def setup_service(self):
        """настройка сервиса драйвера"""
        service = ChromeService(ChromeDriverManager().install())
        return service

    def create_driver(self, options, service):
        """создание экземпляра драйвера"""
        driver = webdriver.Chrome(options=options, service=service)
        return driver

    def navigate_to_url(self, url):
        """переход по указанному URL"""
        self.driver.get(url)

    def set_window_size(self, width, height):
        """установка размера окна браузера"""
        self.driver.set_window_size(width, height)

    def test_open_website(self):
        """главный метод открытия сайта - использует другие методы"""
        options = self.setup_options()
        service = self.setup_service()
        self.driver = self.create_driver(options, service)
        base_url = 'https://www.saucedemo.com/'
        self.navigate_to_url(base_url)
        self.set_window_size(1920, 1080)


start_test = Test() # создаём экземпляр класса
start_test.test_open_website() # вызов метода класса