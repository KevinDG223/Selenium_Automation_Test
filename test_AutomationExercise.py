import json
import pytest
from POM.LogIn import LoginPage

test_data_path = '../project/data/test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance

    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.product_page()
    shop_page.add_product_to_cart(test_list_item["tshirtName"], test_list_item["jeansName"])
    checkout_confirmation = shop_page.go_to_cart()
    checkout_confirmation.do_checkout(test_list_item["cardName"], test_list_item["cardNumber"],test_list_item["cardCvc"], test_list_item["cardMonth"], test_list_item["cardYear"])
    checkout_confirmation.validate_order()
