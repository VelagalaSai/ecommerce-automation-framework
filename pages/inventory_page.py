from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    # Locators
    PRODUCT_TITLES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_page_loaded(self):
        return "inventory" in self.driver.current_url

    def get_all_product_names(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))
        return [item.text for item in items]

    def get_all_product_prices(self):
        prices = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_PRICES))
        return [float(p.text.replace("$", "")) for p in prices]

    def add_first_product_to_cart(self):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTONS))
        buttons[0].click()

    def add_multiple_products_to_cart(self, count):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTONS))
        for i in range(min(count, len(buttons))):
            buttons[i].click()

    def get_cart_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
