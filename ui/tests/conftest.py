import pytest
from playwright.sync_api import sync_playwright
from configuration import BASE_URL, HEADLESS
from ui.pages.home_page import HomePage
from logger_config import setup_logger

setup_logger()


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=HEADLESS)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()


@pytest.fixture
def home_page(page):
    return HomePage(page)
