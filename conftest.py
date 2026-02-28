import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import load_config

from utils.logger import get_logger

logger = get_logger()
logger.info("This is a test log message")

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

        import pytest
from datetime import datetime


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            page.screenshot(path=f"screenshots/{item.name}_{timestamp}.png")