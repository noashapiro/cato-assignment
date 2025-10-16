import allure


class TestDemoBlaze:
    
    @allure.title("Verify all products display with correct details")
    def test_display_all_products_with_correct_details(self, home_page):
        assert home_page.is_page_loaded(), "Home page did not load properly"
        home_page.wait_for_element(home_page.locators.PRODUCT_CARD)
        
        product_count = home_page.get_product_count()
        assert product_count > 0, "No products found on the page"
        
        home_page.validate_product_display()
    
    @allure.title("Login with valid credentials")
    def test_login_with_valid_credentials(self, home_page):
        username = "123"
        home_page.wait_for_element(home_page.locators.PRODUCT_CARD)
        home_page.click_login()
        home_page.fill_login_form(username=username, password="123")
        home_page.submit_login()
        
        logged_in_username = home_page.get_logged_in_username()
        assert username in logged_in_username, (
            f"Expected username '{username}' to appear in '{logged_in_username}'"
        )
    
    @allure.title("Login with empty credentials shows validation error")
    def test_login_with_empty_credentials(self, home_page):
        home_page.wait_for_element(home_page.locators.PRODUCT_CARD)
        home_page.click_login()
        home_page.fill_login_form(username="", password="")
        dialog_message = home_page.submit_login_and_handle_dialog()
        
        assert dialog_message, "Expected dialog to appear but it didn't"
        assert "Please fill out Username and Password." in dialog_message, (
            f"Expected validation message but got: {dialog_message}"
        )
