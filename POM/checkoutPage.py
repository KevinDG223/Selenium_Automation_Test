from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//a[text()='Proceed To Checkout']")
        self.place_order = (By.XPATH, "//a[text()='Place Order']")
        self.card_name = (By.NAME, "name_on_card")
        self.card_number = (By.NAME, "card_number")
        self.card_cvc = (By.NAME, "cvc")
        self.expiry_month = (By.NAME, "expiry_month")
        self.expiry_year = (By.NAME, "expiry_year")
        self.submit_button = (By.ID, "submit")
        self.order_text = (By.XPATH, "//p[contains(text(), 'Your order has been confirmed!')]")


    def do_checkout(self, card_name, card_number,card_cvc, card_month, card_year):
        self.driver.find_element(*self.checkout_button).click()
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.driver.find_element(*self.place_order).click()
        self.driver.find_element(*self.card_name).send_keys(card_name)
        self.driver.find_element(*self.card_number).send_keys(card_number)
        self.driver.find_element(*self.card_cvc).send_keys(card_cvc)
        self.driver.find_element(*self.expiry_month).send_keys(card_month)
        self.driver.find_element(*self.expiry_year).send_keys(card_year)
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        wait = WebDriverWait(self.driver, 10)
        confirmation_element = wait.until(EC.visibility_of_element_located(self.order_text))
        assert "Your order has been confirmed!" in confirmation_element.text