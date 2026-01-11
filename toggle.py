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
base_url = "https://the-internet.herokuapp.com/horizontal_slider" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

actions = ActionChains(driver) # Создаём экземпляр класса

slider = driver.find_element(By.XPATH, "//input[@type='range']")

start_value = driver.find_element(By.XPATH, "//*[@id='range']").text
time.sleep(5)

actions.click_and_hold(slider).move_by_offset(50, 0).release().perform() # Перемещаем ползунок с помощью click_and_hold на определённую длину по x и отпускаем с помощью release
end_value = driver.find_element(By.XPATH, "//*[@id='range']").text

assert float(start_value) != float(end_value), f"Значения положения ползунка совпадают! Первоначальное значение: {start_value}, конечное значение: {end_value}"
# Проводим проверку, сравнивая начальное и конечное значения
print("Toggle move good")