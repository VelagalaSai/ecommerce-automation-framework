import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:

    def login(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        return InventoryPage(driver)

    def test_products_are_displayed(self, driver):
        """Test that products are visible on inventory page"""
        inventory = self.login(driver)
        products = inventory.get_all_product_names()
        assert len(products) > 0, "No products displayed on inventory page"

    def test_product_count_is_six(self, driver):
        """Test that exactly 6 products are displayed"""
        inventory = self.login(driver)
        products = inventory.get_all_product_names()
        assert len(products) == 6, f"Expected 6 products but got {len(products)}"

    def test_products_have_prices(self, driver):
        """Test that all products have valid prices"""
        inventory = self.login(driver)
        prices = inventory.get_all_product_prices()
        assert len(prices) > 0, "No prices found"
        for price in prices:
            assert price > 0, f"Invalid price found: {price}"

    def test_add_single_product_to_cart(self, driver):
        """Test adding one product to cart updates badge"""
        inventory = self.login(driver)
        inventory.add_first_product_to_cart()
        count = inventory.get_cart_count()
        assert count == 1, f"Expected cart count 1 but got {count}"

    def test_add_multiple_products_to_cart(self, driver):
        """Test adding 3 products to cart"""
        inventory = self.login(driver)
        inventory.add_multiple_products_to_cart(3)
        count = inventory.get_cart_count()
        assert count == 3, f"Expected cart count 3 but got {count}"

    def test_navigate_to_cart(self, driver):
        """Test clicking cart icon navigates to cart page"""
        inventory = self.login(driver)
        inventory.add_first_product_to_cart()
        inventory.go_to_cart()
        assert "cart" in driver.current_url, "Did not navigate to cart page"
