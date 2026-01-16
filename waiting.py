import time

from faker import Faker
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


name_locators = {
    1: "//*[@id='item_4_title_link']/div",
    2: "//*[@id='item_0_title_link']/div",
    3: "//*[@id='item_1_title_link']/div",
    4: "//*[@id='item_5_title_link']/div",
    5: "//*[@id='item_2_title_link']/div",
    6: "//*[@id='item_3_title_link']/div",
}
add_to_cart_locators = {
    1: "//*[@id='add-to-cart-sauce-labs-backpack']",
    2: "//*[@id='add-to-cart-sauce-labs-bike-light']",
    3: "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']",
    4: "//*[@id='add-to-cart-sauce-labs-fleece-jacket']",
    5: "//*[@id='add-to-cart-sauce-labs-onesie']",
    6: "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
}


def get_product_info(info_xpath, price_info):
    product = driver.find_element(By.XPATH, info_xpath)
    value_product = product.text

    price_product = driver.find_element(By.XPATH, price_info)
    value_price_product = price_product.text

    return value_product, value_price_product


def check_product_info(info_xpath, price_xpath, expected_product, expected_price):
    actual_product, actual_price = get_product_info(info_xpath, price_xpath)
    print(f"Название: {actual_product}, Цена: {actual_price}")

    assert actual_product == expected_product, f"Название не совпадает: {actual_product} != {expected_product}"
    assert actual_price == expected_price, f"Цена не совпадает: {actual_price} != {expected_price}"

    return actual_product, actual_price


try:
    print("Приветствую тебя в нашем интернет - магазине")
    print("Выбери один из следующих товаров и укажи его номер:\n 1 - Sauce Labs Backpack,"
          "\n 2 - Sauce Labs Bike Light,\n 3 - Sauce Labs Bolt T-Shirt,\n 4 - Sauce Labs Fleece Jacket,"
          "\n 5 - Sauce Labs Onesie,\n 6 - Test.allTheThings() T-Shirt (Red)")
    driver.implicitly_wait(16)
    product_index = int(input())
    if 1 <= product_index <= 6:
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
        value_product_1, value_price_product_1 = get_product_info(name_locators[product_index], f"//div[@class='inventory_item'][{product_index}]//div[@class='inventory_item_price']")
        print(value_product_1 + " = " + value_price_product_1)
        driver.find_element(By.XPATH, add_to_cart_locators[product_index]).click() # Добавляем продукт в корзину
        print("Select Product 1")  # Выбираем продукт


        cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
        cart.click()
        print("Enter Cart") # Переходим в корзину

        value_cart_product_1, value_price_cart_product_1 = check_product_info(name_locators[product_index], f"//div[@class='inventory_item_price']", value_product_1, value_price_product_1)
        print(value_cart_product_1 + " / " + value_price_cart_product_1)
        print("Info Cart + Price Cart Product 1 good")  # Отчёт о корректности инфы о продукте в корзине


        checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
        checkout.click()
        print("Click Checkout")

        fake = Faker("en_US")  # На английском языке, для русского - Faker("ru_RU")

        name = fake.first_name()  # Генерируем случайное имя
        surname = fake.last_name()  # Генерируем случайную фамилию
        postal = fake.postalcode()  # Генерируем случайный postal code

        driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys(name)
        print("Input First Name")

        driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys(surname)
        print("Input Last Name")

        driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys(postal)
        print("Input Postal Code")

        driver.find_element(By.XPATH, "//*[@id='continue']").click()
        print("Click Continue")

        value_finish_product_1, value_price_finish_product_1 = check_product_info(name_locators[product_index], f"//div[@class='inventory_item_price']", value_product_1, value_price_product_1)
        print(value_finish_product_1 + " ; " + value_price_finish_product_1)
        print("Info Finish + Price Finish Product 1 good") # Производим проверку названия и цены товара в финальном окне обзора


        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
        value_summary_price = summary_price.text
        print(value_summary_price)
        item_total = "Item total: $" + str(float(value_price_finish_product_1[1:]))
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
        print("Finish test")
    else:
        print("Выбрано число вне диапазона 1 - 6!")
except ValueError:
    print("Ваш ответ должен быть в виде числа (1 - 6)")
except TimeoutError:
    print("Превышено время ожидания. Попробуйте ещё")
driver.close()