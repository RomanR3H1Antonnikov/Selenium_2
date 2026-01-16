import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage


class Test: # общий класс, который будет содержать метод для работы в данном тесте


    def __init__(self):
        self.driver = None


    def test_open_website(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        self.driver.get(base_url)
        self.driver.set_window_size(1920, 1080)

        login = LoginPage(self.driver)
        login.authorization(login_name="standard_user", login_password="secret_sauce")

        time.sleep(3)


    def test_select_product(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']"))).click()
        print("Click Select Product")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='shopping_cart_link']"))).click()
        print("Enter Shopping Cart")  # Переходим в корзину

        value_success_test = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='title']"))).text
        assert value_success_test == 'Your Cart', "Ошибка! Вход в корзину не выполнен!"
        print("Test Success")


start_test = Test() # создаём экземпляр класса
try:
    start_test.test_open_website() # вызов метода класса
    start_test.test_select_product()
except Exception as e:
    print(f"Ошибка: {e}")