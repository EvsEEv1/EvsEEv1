from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.login_loc = (By.ID, "user-name")
        self.login_button_loc = (By.ID, "login-button")
        self.password_loc = (By.ID, "password")
        
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        
    def enter_username(self, username):
        self.driver.find_element(*self.login_loc).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(*self.password_loc).send_keys(password)
    
    def click_login(self):
       self.driver.find_element(*self.login_button_loc).click()
       