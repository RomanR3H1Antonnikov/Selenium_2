import time

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


def get_product_info(info_xpath, price_xpath):
    product = driver.find_element(By.XPATH, info_xpath)
    value_product = product.text

    price_product = driver.find_element(By.XPATH, price_xpath)
    value_price_product = price_product.text

    return value_product, value_price_product


def check_product_info(info_xpath, price_xpath, expected_product, expected_price):
    actual_product, actual_price = get_product_info(info_xpath, price_xpath)
    print(f"Название: {actual_product}, Цена: {actual_price}")

    assert actual_product == expected_product, f"Название не совпадает: {actual_product} != {expected_product}"
    assert actual_price == expected_price, f"Цена не совпадает: {actual_price} != {expected_price}"

    return actual_product, actual_price


user_name = driver.find_element(By.ID, "user-name") # поиск локатора поля ввода имени пользователя по ID
user_name.send_keys('standard_user')
print("Input Login")

password = driver.find_element(By.ID, "password") # поиск локатора поля ввода пароля по ID
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.ID, "login-button") # поиск локатора кнопки по ID
button_login.click() # Используем метод .click() для авторизации на сайте
print("Click Login Button")

time.sleep(5) # Пауза для нажатия на кнопку "Ок" при всплывающем уведомлении об утечке пароля
value_product_1, value_price_product_1 = get_product_info("//*[@id='item_4_title_link']/div", "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
print(value_product_1 + " = " + value_price_product_1)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click() # Добавляем продукт 1 в корзину
print("Select Product 1")  # Выбираем продукт 1


value_product_2, value_price_product_2 = get_product_info("//*[@id='item_0_title_link']/div", "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
print(value_product_2 + " = " + value_price_product_2)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click() # Добавляем продукт 2 в корзину
print("Select Product 2")  # Выбираем продукт 2


cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
cart.click()
print("Enter Cart") # Переходим в корзину

value_cart_product_1, value_price_cart_product_1 = check_product_info("//*[@id='item_4_title_link']/div", "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div", value_product_1, value_price_product_1)
print(value_cart_product_1 + " / " + value_price_cart_product_1)
print("Info Cart + Price Cart Product 1 good")  # Отчёт о корректности инфы о продукте 1 в корзине

value_cart_product_2, value_price_cart_product_2 = check_product_info("//*[@id='item_0_title_link']/div", "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div", value_product_2, value_price_product_2)
print(value_cart_product_2 + " / " + value_price_cart_product_2)
print("Info Cart + Price Cart Product 2 good")  # Отчёт о корректности инфы о продукте 2 в корзине

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

value_finish_product_1, value_price_finish_product_1 = check_product_info("//*[@id='item_4_title_link']/div", "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div", value_product_1, value_price_product_1)
print(value_finish_product_1 + " ; " + value_price_finish_product_1)
print("Info Finish + Price Finish Product 1 good") # Производим проверку названия и цены товара 1 в финальном окне обзора

value_finish_product_2, value_price_finish_product_2 = check_product_info("//*[@id='item_0_title_link']/div", "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div", value_product_2, value_price_product_2)
print(value_finish_product_2 + " ; " + value_price_finish_product_2)
print("Info Finish + Price Finish Product 2 good") # Производим проверку названия и цены товара 2 в финальном окне обзора

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = "Item total: $" + str(float(value_price_finish_product_1[1:]) + float(value_price_finish_product_2[1:]))
print(item_total)
assert value_summary_price == item_total # Производим проверку суммы всех товаров в финальном окне просмотра
print("Total Summary Price good")

button_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
button_finish.click()
print("Click Finish")

time.sleep(3) # Пауза для ожидания подгрузки страницы

checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == "Thank you for your order!"  # Производим проверку появления окна с сообщением об успешном заказе
print("Info Order Complete")