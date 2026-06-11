import pytest
from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, driver):
        """Test login with valid credentials"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert login.is_login_successful(), "Login failed with valid credentials"

    def test_invalid_password(self, driver):
        """Test login with wrong password shows error"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "wrong_password")
        error = login.get_error_message()
        assert "Username and password do not match" in error, "Error message not shown"

    def test_empty_username(self, driver):
        """Test login with empty username shows error"""
        login = LoginPage(driver)
        login.open()
        login.login("", "secret_sauce")
        error = login.get_error_message()
        assert "Username is required" in error, "Error message not shown for empty username"

    def test_empty_password(self, driver):
        """Test login with empty password shows error"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "")
        error = login.get_error_message()
        assert "Password is required" in error, "Error message not shown for empty password"

    def test_locked_out_user(self, driver):
        """Test locked out user cannot login"""
        login = LoginPage(driver)
        login.open()
        login.login("locked_out_user", "secret_sauce")
        error = login.get_error_message()
        assert "locked out" in error.lower(), "Locked out error not shown"

    def test_logout(self, driver):
        """Test user can logout successfully"""
        from pages.inventory_page import InventoryPage
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert login.is_login_successful()
        inventory = InventoryPage(driver)
        inventory.logout()
        assert driver.current_url == LoginPage.URL + "/" or driver.current_url == LoginPage.URL
