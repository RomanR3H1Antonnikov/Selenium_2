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
base_url = "https://www.lambdatest.com/selenium-playground/upload-file-demo" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

path_upload = "D:\\Programming\\Selenium_2\\UPLOAD\\Cup.png"

click_button = driver.find_element(By.XPATH, "//input[@id='file']")
click_button.send_keys(path_upload)

driver.close()