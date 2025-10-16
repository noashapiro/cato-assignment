import logging
from playwright.sync_api import Page
from ui.pages.base_page import BasePage
from ui.locators.home_page_locators import HomePageLocators

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HomePageLocators()
    
    def is_page_loaded(self) -> bool:
        return super().is_page_loaded(self.locators.NAVBAR_BRAND)
    
    def get_product_count(self) -> int:
        count = self.page.locator(self.locators.PRODUCT_CARD).count()
        logger.info(f"Found {count} products")
        return count
    
    def get_product_details(self, index: int = 0) -> dict:
        product_card = self.page.locator(self.locators.PRODUCT_CARD).nth(index)
        name = product_card.locator(self.locators.PRODUCT_NAME).text_content()
        price = product_card.locator(self.locators.PRODUCT_PRICE).text_content()
        
        return {
            "name": name.strip() if name else "",
            "price": price.strip() if price else ""
        }
    
    def validate_product_display(self):
        products_count = self.get_product_count()
        
        for i in range(products_count):
            product = self.get_product_details(i)
            
            assert product["name"], f"Product {i} name is empty"
            assert product["price"], f"Product {i} price is empty"
            assert "$" in product["price"], f"Product {i} price doesn't contain $"
        
        logger.info(f"Validated {products_count} products")
    
    def click_login(self):
        logger.info("Opening login modal")
        self.page.locator(self.locators.LOGIN_BUTTON).click()
    
    def fill_login_form(self, username: str, password: str):
        logger.info(f"Filling login form with username: '{username}'")
        self.page.locator(self.locators.LOGIN_USERNAME_FIELD).fill(username)
        self.page.locator(self.locators.LOGIN_PASSWORD_FIELD).fill(password)
    
    def submit_login(self):
        logger.info("Submitting login form")
        self.page.get_by_role("button", name="Log in").click()
    
    def get_logged_in_username(self) -> str:
        self.page.wait_for_selector(self.locators.LOGGED_IN_USERNAME)
        username = self.page.locator(self.locators.LOGGED_IN_USERNAME).inner_text()
        logger.info(f"User logged in: {username}")
        return username
    
    def submit_login_and_handle_dialog(self) -> str:
        self.page.wait_for_selector(self.locators.LOGIN_USERNAME_FIELD, state="visible")
        
        dialog_message = ""
        
        def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            logger.info(f"Dialog appeared: {dialog_message}")
            dialog.accept()
        
        self.page.once("dialog", handle_dialog)
        self.page.locator(self.locators.LOGIN_SUBMIT_BUTTON).click()
        self.page.wait_for_timeout(500)
        
        return dialog_message
