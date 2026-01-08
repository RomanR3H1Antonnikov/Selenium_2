import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Импорт используемых библиотек

# Настройка драйвера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://demoqa.com/buttons" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

action = ActionChains(driver) # Создаём экземпляр класса
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click_button).perform() # Производим двойной клик
print("Произвели двойной клик")

right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click_button).perform() # Производим клик правой кнопкой мыши
print("Произвели клик правой клавишей")