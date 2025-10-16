import pytest
from playwright.sync_api import expect
import pytest
from playwright.sync_api import sync_playwright
from configuration import BASE_URL
from ui.pages import home_page



class TestHomePage:
    def test_display_all_products_with_correct_details(self, home_page):
        assert home_page.is_page_loaded(), "Home page did not load properly"

        home_page.wait_for_element(home_page.product_cards)

        product_count = home_page.get_product_count()
        assert product_count > 0, "No products found on the page"

        home_page.validate_product_display()