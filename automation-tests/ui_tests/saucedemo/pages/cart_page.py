from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage():
    def __init__(self, driver):
        self.driver = driver 
        self.inventory_item_name_loc = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_loc = (By.CLASS_NAME, "cart_item")
        self.chkout_btn_loc = (By.ID, "checkout")
    
    def get_cart_items(self):
        cart_elements = self.driver.find_elements(*self.inventory_item_name_loc)
        return [el.text for el in cart_elements]
        
    def checkout(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ESCAPE)
        wait = WebDriverWait(self.driver, 5)
        checkout_btn = wait.until(EC.element_to_be_clickable(self.chkout_btn_loc))
        checkout_btn.click()