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
base_url = "https://the-internet.herokuapp.com/javascript_alerts" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

click_alert_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button")
click_alert_button.click()
print("click_alert_button") # Нажимаем на кнопку
time.sleep(3)
driver.switch_to.alert.accept() # Нажимаем на кнопку ок внутри

click_confirm_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button")
click_confirm_button.click()
print("click_confirm_button") # Нажимаем на кнопку
time.sleep(3)
driver.switch_to.alert.dismiss() # Нажимаем на кнопку отмена внутри

click_promt_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button")
click_promt_button.click()
print("click_promt_button") # Нажимаем на кнопку
time.sleep(3)
driver.switch_to.alert.send_keys("Hello World!") # вводим фразу в поле
driver.switch_to.alert.accept() # Нажимаем на кнопку ок внутри

driver.close()