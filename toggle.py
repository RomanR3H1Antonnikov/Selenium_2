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
base_url = "https://html5css.ru/howto/howto_js_rangeslider.php" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

actions = ActionChains(driver)

slider = driver.find_element(By.XPATH, "//input[@class='slider-color']")

time.sleep(5)

actions.click_and_hold(slider).move_by_offset(-500, 0).release().perform()

# здесь должна быть реализована проверка, что расстояние перемещения совпадает с тем,
# которое отображается в соответствующем поле на сайте, однако сервер не позволяет загрузить сайт (скрин прикрепил к ответу на заданию)