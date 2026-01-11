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
print(f"Начальное значение ползунка: {start_value}")
time.sleep(2)

pixels_per_step = 129 / ((5.0 - 0.0) / 0.5)
print(f"Один шаг значения ({0.5}) = {pixels_per_step:.1f} пикселя")

target_value = 5.0
print(f"Целевое значение для теста: {target_value}")

x = (target_value - float(start_value)) / 0.5 * pixels_per_step
print(f"Смещение для значения {target_value}: {x:.1f} пикселей")

actions.click_and_hold(slider).move_by_offset(x, 0).release().perform() # Перемещаем ползунок с помощью click_and_hold на определённую длину по x и отпускаем с помощью release
end_value = driver.find_element(By.XPATH, "//*[@id='range']").text

try:
    end_value_float = float(end_value)
    assert round(end_value_float, 1) == target_value, (
        f"Ползунок установился в неверную позицию! "
        f"Ожидалось: {target_value}, Получено: {end_value_float}"
    )
    print(f"Toggle move good, ползунок в значении {target_value}")
except ValueError:
    print("Не удалось преобразовать значение в число!")
except AssertionError as e:
    print(f"Тест не прошёл, Ошибка: {e}")

driver.close()