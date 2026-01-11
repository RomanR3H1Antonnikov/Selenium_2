import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Импорт используемых библиотек

# Настройка драйвера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://www.lambdatest.com/selenium-playground/iframe-demo/" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)
input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]")
value_pole = input_pole.text
print(value_pole)

input_pole.send_keys(Keys.CONTROL + "a")

click_editing_panel_bold = driver.find_element(By.XPATH, "//button[@title='Bold']")
click_editing_panel_bold.click()
print('Click editing panel bold')

click_editing_panel_italic = driver.find_element(By.XPATH, "//button[@title='Italic']")
click_editing_panel_italic.click()
print('Click editing panel italic')

click_editing_panel_strikethrough = driver.find_element(By.XPATH, "//button[@title='Strike through']")
click_editing_panel_strikethrough.click()
print('Click editing panel strike through')

new_input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/b")
value_input_pole = new_input_pole.text
print(value_input_pole)
assert value_pole == value_input_pole
print("Редактирование успешно")

time.sleep(10)
driver.quit()