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
base_url = "https://demoqa.com/radio-button" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

radio_button = driver.find_element(By.XPATH, "(//label[@class='custom-control-label'])[2]")
radio_button.click()
assert driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div[2]/p/span").text == "Impressive"
print("Radio Button Active")