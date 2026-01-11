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
base_url = "https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_drop.click()
time.sleep(3)

select_country = driver.find_element(By.XPATH, "//li[@class='select2-results__option'][3]")
aim_country = select_country.text
select_country.click()

final_country = driver.find_element(By.XPATH, "//span[@class='select2-selection__rendered']").text
assert aim_country == final_country, f"Значения не совпадают! Выбираемая страна: {aim_country}, выбранная страна: {final_country}"

driver.close()