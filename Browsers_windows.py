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
base_url = "https://demoqa.com/browser-windows" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

new_tab = driver.find_element(By.XPATH, "//button[@id='tabButton']")
new_tab.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])

new_window = driver.find_element(By.XPATH, "//button[@id='windowButton']")
new_window.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.switch_to.window(driver.window_handles[2])

driver.quit()