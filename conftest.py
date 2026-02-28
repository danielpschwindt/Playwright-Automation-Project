import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import load_config


@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture(scope="function")
def page(config):
    with sync_playwright() as p:
        browser_type = getattr(p, config["browser"])
        browser = browser_type.launch(headless=config["headless"])
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()