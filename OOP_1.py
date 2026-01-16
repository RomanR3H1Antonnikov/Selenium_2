from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Test(): # общий класс, который будет содержать метод для работы в данном тесте
    def test_select_product(self):
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.set_window_size(1920, 1080)


start_test = Test() # создаём экземпляр класса
start_test.test_select_product() # вызов метода класса