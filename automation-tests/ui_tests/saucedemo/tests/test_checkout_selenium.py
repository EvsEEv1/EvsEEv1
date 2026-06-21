from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage, OverviewPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import pytest

@pytest.mark.selenium
def test_buy_backpack(driver):
    
    login = LoginPage(driver)
    login.open()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

   
    inventory = InventoryPage(driver)
    assert inventory.get_title() == "Products"
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.go_to_cart()

    
    cart = CartPage(driver)
    assert "Sauce Labs Backpack" in cart.get_cart_items(), "Либо неверный предмет, либо предмета нет"
    cart.checkout()
    
    check = CheckoutPage(driver)
    check.fill_forms("Mr","Client","125abcd")
    check.continue_checkout()
    
    overview = OverviewPage(driver)
    
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)

    overview.finish()
    assert overview.get_complete_message() == "Thank you for your order!", "Неверный текст сообщения/Сбой"
    