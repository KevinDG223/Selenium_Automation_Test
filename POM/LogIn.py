from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.shopPage import ShopPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = (By.CSS_SELECTOR, "a[href='/login']")
        self.username_input = (By.CSS_SELECTOR, "[data-qa='login-email']")
        self.password_input = (By.CSS_SELECTOR, "[data-qa='login-password']")
        self.sign_button = (By.CSS_SELECTOR, "[data-qa='login-button']")




    def login(self, username, password):
        self.driver.find_element(*self.login_page).click()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page
