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


user_name = driver.find_element(By.ID, "user-name") # поиск локатора поля ввода имени пользователя по ID
user_name.send_keys('standard_user')
print("Input Login")

password = driver.find_element(By.ID, "password") # поиск локатора поля ввода пароля по ID
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.ID, "login-button") # поиск локатора кнопки по ID
button_login.click() # Используем метод .click() для авторизации на сайте
print("Click Login Button")


button_add_backpack = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
button_cart_link = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

time.sleep(2)
driver.back() # Возвращаемся на страницу каталога с помощью метода back()
print("Click Back")

time.sleep(2)
driver.forward() # Возвращаемся на страницу корзины с помощью метода forward()
print("Click Forward")