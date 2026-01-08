from logging import lastResort, debug
from typing import final

from requests.utils import select_proxy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Импорт используемых библиотек

# Настройка драйвера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://www.saucedemo.com/" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

user_name = driver.find_element(By.ID, "user-name") # поиск локатора поля ввода имени пользователя по ID
user_name.send_keys('standard_user')
print("Input Login")

password = driver.find_element(By.ID, "password") # поиск локатора поля ввода пароля по ID
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.ID, "login-button") # поиск локатора кнопки по ID
button_login.click() # Используем метод .click() для авторизации на сайте
print("Click Login Button")

product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product.click()
print("Select Product 1") # Выбираем продукт 1

cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
cart.click()
print("Enter Cart") # Переходим в корзину

cart_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1 # Производим проверку названия товара в корзине
print("Info Cart Product 1 good")

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print(value_price_cart_product_1)
assert value_price_product_1 == value_price_cart_product_1 # Производим проверку стоимости товара в корзине
print("Price Cart Product 1 good")

checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
checkout.click()
print("Click Checkout")

first_name = driver.find_element(By.XPATH, "//*[@id='first-name']")
first_name.send_keys("Roman")
print("Input First Name")

last_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
last_name.send_keys("Antonnikov")
print("Input Last Name")

postal_code = driver.find_element(By.XPATH, "//*[@id='postal-code']")
postal_code.send_keys(12345)
print("Input Postal Code")

button_continue = driver.find_element(By.XPATH, "//*[@id='continue']")
button_continue.click()
print("Click Continue")

finish_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1 # Производим проверку названия товара в финальном окне обзора
print("Info Finish Product 1 good")

price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_finish_product_1 = price_finish_product_1.text
print(value_price_finish_product_1)
assert value_price_finish_product_1 == value_price_product_1 # Производим проверку цены товара в финальном окне обзора
print("Info Finish Price Product 1 good")

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = "Item total: " + value_price_finish_product_1
print(item_total)
assert value_summary_price == item_total # Производим проверку суммы всех товаров в финальном окне просмотра
print("Total Summary Price good")

button_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
button_finish.click()
print("Click Finish")

checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == "Thank you for your order!"  # Производим проверку появления окна с сообщением об успешном заказе
print("Info Order Complete")