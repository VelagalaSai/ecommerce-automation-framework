import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope="function")
def driver():
    """Setup and teardown Edge browser for each test"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def pytest_configure(config):
    """Configure pytest HTML report"""
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
