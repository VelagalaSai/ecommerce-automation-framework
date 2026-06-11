import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:

    def login_and_add_products(self, driver, count=2):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        inventory = InventoryPage(driver)
        inventory.add_multiple_products_to_cart(count)
        inventory.go_to_cart()
        return CartPage(driver)

    def test_cart_page_loads(self, driver):
        """Test cart page loads correctly"""
        cart = self.login_and_add_products(driver)
        assert cart.is_page_loaded(), "Cart page did not load"

    def test_cart_shows_added_items(self, driver):
        """Test items added are visible in cart"""
        cart = self.login_and_add_products(driver, 2)
        items = cart.get_cart_items()
        assert len(items) == 2, f"Expected 2 items in cart but found {len(items)}"

    def test_remove_item_from_cart(self, driver):
        """Test removing an item from cart"""
        cart = self.login_and_add_products(driver, 2)
        initial_count = cart.get_cart_item_count()
        cart.remove_first_item()
        new_count = cart.get_cart_item_count()
        assert new_count == initial_count - 1, "Item was not removed from cart"

    def test_checkout_flow(self, driver):
        """Test complete checkout flow"""
        cart = self.login_and_add_products(driver, 1)
        cart.click_checkout()
        cart.fill_checkout_info("Sai", "Bhaskari", "500001")
        cart.click_finish()
        confirmation = cart.get_order_confirmation()
        assert "Thank you" in confirmation, f"Order confirmation not shown. Got: {confirmation}"

    def test_empty_cart(self, driver):
        """Test cart is empty when no items added"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        inventory = InventoryPage(driver)
        inventory.go_to_cart()
        cart = CartPage(driver)
        count = cart.get_cart_item_count()
        assert count == 0, f"Expected empty cart but found {count} items"
