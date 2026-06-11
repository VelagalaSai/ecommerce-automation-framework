from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button.btn_secondary.cart_button")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ORDER_CONFIRM = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_page_loaded(self):
        return "cart" in self.driver.current_url

    def get_cart_items(self):
        try:
            items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_NAMES))
            return [item.text for item in items]
        except:
            return []

    def get_cart_item_count(self):
        try:
            items = self.driver.find_elements(*self.CART_ITEMS)
            return len(items)
        except:
            return 0

    def remove_first_item(self):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.REMOVE_BUTTONS))
        buttons[0].click()

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    def get_order_confirmation(self):
        try:
            msg = self.wait.until(EC.presence_of_element_located(self.ORDER_CONFIRM))
            return msg.text
        except:
            return ""
          
