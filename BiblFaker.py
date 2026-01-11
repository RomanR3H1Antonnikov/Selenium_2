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

fake = Faker("en_US") # На английском языке, для русского - Faker("ru_RU")

name = fake.first_name() # Генерируем случайный юзернейм
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(name)
print("Input login")

time.sleep(10)
driver.quit()