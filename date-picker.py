import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Импорт используемых библиотек

# Настройка драйвера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://demoqa.com/date-picker" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
date_input.send_keys(Keys.CONTROL + "a")
date_input.send_keys(Keys.DELETE)

time.sleep(1)

current_date = datetime.now()
date_10_days_later = current_date + timedelta(days=10)

date_input.send_keys(date_10_days_later.strftime("%d.%m.%Y"))