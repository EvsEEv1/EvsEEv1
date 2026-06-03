from selenium.webdriver.common.by import By 

class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver
        self.first_name_loc = (By.ID, "first-name")
        self.last_name_loc = (By.ID, "last-name")
        self.postal_code_loc = (By.ID, "postal-code")
        self.continue_btn_loc = (By.ID, "continue")
        
    def fill_forms(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_loc).send_keys(first_name)
        self.driver.find_element(*self.last_name_loc).send_keys(last_name)
        self.driver.find_element(*self.postal_code_loc).send_keys(postal_code)

        
    def continue_checkout(self):
        self.driver.find_element(*self.continue_btn_loc).click()        
        
class OverviewPage():
    def __init__(self, driver):
        self.driver = driver
        self.finish_btn_loc = (By.ID, "finish")
        self.finish_header = (By.CLASS_NAME, "complete-header")
        
    def finish(self):
        self.driver.find_element(*self.finish_btn_loc).click()
        
    def get_complete_message(self):
        return self.driver.find_element(*self.finish_header).text
        