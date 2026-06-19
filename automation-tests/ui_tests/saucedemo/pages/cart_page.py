from selenium.webdriver.common.by import By

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
        self.driver.find_element(*self.chkout_btn_loc).click()
        