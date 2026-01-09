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
base_url = "https://demoqa.com/checkbox" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
check_box.click()
input_check_box = driver.find_element(By.XPATH, "//input[@id='tree-node-home']") # Находим элемент через input, а не span,
# тк класс вроде span и div всегда будет возвращать False в методе is_selected() (тк не обладает атрибутами <select> или checked)
assert input_check_box.is_selected(), "Чек-бокс не выбран!!"
print("Чек-бокс выбран")
