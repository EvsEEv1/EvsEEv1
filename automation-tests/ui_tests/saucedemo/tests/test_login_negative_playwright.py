import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

def test_login_empty_username(browser):
    """Вход с пустым полем имени пользователя."""
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/", wait_until="domcontentloaded")

    page.fill("#user-name", "")
    page.fill("#password", "secret_sause")
    page.click("#login-button")

    error_element = page.locator("[data-test='error']") 
    
    assert error_element.is_visible()
    assert "Username is required" in error_element.text_content()


def test_login_empty_password(browser):
    """Вход с пустым полем пароля."""
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/", wait_until="domcontentloaded")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "")
    page.click("#login-button")

    error_element = page.locator("[data-test='error']") 
    
    assert error_element.is_visible()
    assert "Password is required" in error_element.text_content()

def test_login_wrong_credentials(browser):  
    """Вход с неверными данными"""  
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/", wait_until="domcontentloaded")

    page.fill("#user-name", "wrong_login")
    page.fill("#password", "wrong_password")
    page.click("#login-button")

    error_element = page.locator("[data-test='error']") 
    
    assert error_element.is_visible()
    assert "Username and password do not match any user in this service" in error_element.text_content()


def test_login_locked_out_user(browser):  
    """Вход с неверными данными"""  
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/", wait_until="domcontentloaded")
    
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    error_element = page.locator("[data-test='error']") 
    
    assert error_element.is_visible()
    assert "Sorry, this user has been locked out." in error_element.text_content()
