from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():


    def __init__(self, driver):
        self.driver = driver


    def authorization(self, login_name, login_password):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
            "//*[@id='user-name']"))).send_keys(login_name)
        print("Input User Name")

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
            "//input[@id='password']"))).send_keys(login_password)
        print("Input Password")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
        print("Click Login Button")