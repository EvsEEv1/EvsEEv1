import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        yield browser
        browser.close()

def test_successful_login_playwright(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")

    # Заполняем логин и пароль
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

   
    page.wait_for_selector(".title")
    title = page.text_content(".title")
    assert title == "Products"

    page.close()