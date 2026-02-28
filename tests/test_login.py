from pages.login_page import LoginPage


def test_valid_login(page, config):
    login_page = LoginPage(page)
    login_page.navigate(config["base_url"])
    login_page.login(config["username"], config["password"])

    assert "inventory" in page.url


def test_invalid_login(page, config):
    login_page = LoginPage(page)
    login_page.navigate(config["base_url"])
    login_page.login("invalid_user", "wrong_password")

    error_message = login_page.get_error_message()
    assert "Epic sadface" in error_message
    
# add assert "this_will_fail" in page.url for a failing test case

from utils.logger import get_logger

logger = get_logger()
logger.info("This is a test log message")
