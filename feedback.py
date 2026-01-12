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
base_url = "https://www.lambdatest.com/selenium-playground/simple-form-demo" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

input_message = driver.find_element(By.XPATH, "//input[@id='user-message']")
message = 'Hello World!'
input_message.send_keys(message)
first_click_button = driver.find_element(By.XPATH, "//button[@id='showInput']")
first_click_button.click()
time.sleep(3)

your_message = driver.find_element(By.XPATH, "//*[@id='message']")
value_message = your_message.text
assert value_message == message
print("Значения верны!")

first_value = 123
second_value = 101
sum_result = first_value + second_value

input_first_value = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_first_value.send_keys(str(first_value))
input_second_value = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_second_value.send_keys(str(second_value))

second_click_button = driver.find_element(By.XPATH, "//*[@id='gettotal']/button")
second_click_button.click()
time.sleep(3)

result = driver.find_element(By.XPATH, "//p[@id='addmessage']")
value_result = result.text
assert value_result == str(sum_result), f"Ошибка! Результат ({value_result}) не совпадает с фактической суммой ({sum_result})!"
print("Values are equal")

driver.close()