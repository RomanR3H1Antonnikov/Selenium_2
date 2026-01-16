import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Test(): # общий класс, который будет содержать метод для работы в данном тесте

    def test_select_product(self):
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.set_window_size(1920, 1080)

        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        user_name.send_keys("standard_user")

        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys("secret_sauce")
        print("Input Password")

        button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()  # Используем метод .click() для авторизации на сайте
        print("Click Login Button")
        
        time.sleep(3)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click Select Product")

        cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='shopping_cart_link']")))
        cart.click()
        print("Enter Shopping Cart")  # Переходим в корзину

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print("Test Success")

start_test = Test() # создаём экземпляр класса
start_test.test_select_product() # вызов метода класса