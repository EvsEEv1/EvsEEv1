from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.title_loc = (By.CLASS_NAME, "title")

    def get_title(self):
        return self.driver.find_element(*self.title_loc).text

    def add_product_to_cart(self, name_of_product: str):
        # product_name — например "Sauce Labs Backpack"
        # Локатор кнопки "Add to cart" у конкретного товара
        id_of_product_btn = f"add-to-cart-{name_of_product.lower().replace(' ', '-')}"
        add_button = (By.ID, id_of_product_btn)
        self.driver.find_element(*add_button).click()
        return id_of_product_btn

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()