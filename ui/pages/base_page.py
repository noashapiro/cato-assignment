from playwright.sync_api import Page
from configuration import BASE_URL, DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL

    def wait_for_element(self, selector: str, timeout: int = DEFAULT_TIMEOUT):
        self.page.wait_for_selector(selector, timeout=timeout)