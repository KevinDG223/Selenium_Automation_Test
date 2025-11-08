from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.checkoutPage import CheckoutPage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_link = (By.CSS_SELECTOR, "a[href='/products']")
        self.men_link = (By.XPATH, "//a[normalize-space()='Men']//i[@class='fa fa-plus']")
        self.tshirt_link = (By.CSS_SELECTOR, "a[href='/category_products/3']")
        self.select_product = (By.CSS_SELECTOR, ".features_items .col-sm-4")
        self.product_info = (By.CSS_SELECTOR, ".productinfo p")
        self.cart_button = (By.CSS_SELECTOR, ".productinfo .btn.btn-default.add-to-cart")
        self.continue_shopping = (By.XPATH, "//button[text()='Continue Shopping']")
        self.jeans_link = (By.CSS_SELECTOR, "a[href='/category_products/6']")
        self.cart_link = (By.CSS_SELECTOR, "a[href='/view_cart']")


    def product_page(self):
        self.driver.find_element(*self.product_link).click()
        self.driver.find_element(*self.men_link).click()
        self.driver.find_element(*self.tshirt_link).click()

    def add_product_to_cart(self, tshirt_name, jeans_name):
        wait = WebDriverWait(self.driver, 10)
        tshirts = self.driver.find_elements(*self.select_product)
        for tshirt in tshirts:
            productName = tshirt.find_element(*self.product_info).text
            if productName == tshirt_name:
                tshirt.find_element(*self.cart_button).click()
                print(f"'{productName}' added to cart.")
                break

        wait.until(EC.element_to_be_clickable(self.continue_shopping)).click()
        self.driver.find_element(*self.men_link).click()
        self.driver.find_element(*self.jeans_link).click()

        jeans = self.driver.find_elements(*self.select_product)
        for jean in jeans:
            productName = jean.find_element(*self.product_info).text
            if productName == jeans_name:
                jean.find_element(*self.cart_button).click()
                print(f"'{productName}' added to cart.")

        wait.until(EC.element_to_be_clickable(self.continue_shopping)).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
        checkout = CheckoutPage(self.driver)
        return checkout
