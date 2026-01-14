import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Импорт используемых библиотек

path_download = "D:\\Programming\\Selenium_2\\files_download"

# Настройка драйвера
options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path_download}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://www.lambdatest.com/selenium-playground/download-file-demo" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

click_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
click_button.click()
time.sleep(3)

file_name = "LambdaTest.pdf"
file_path = path_download + file_name
assert os.access(file_path, os.F_OK) == True, "Файл не в директории!"
print("Файл в директории")

files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("Файл не пуст")
    else:
        print("Файл пуст!")

for file in files:
    os.remove(file)

driver.close()