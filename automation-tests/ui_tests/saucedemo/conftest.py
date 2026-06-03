import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    browser.implicitly_wait(5)  
    yield browser
    browser.quit()