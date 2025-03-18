import pytest
from playwright.sync_api import Playwright, sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture
def api_request_context(playwright_instance):
    request_context = playwright_instance.request.new_context()
    yield request_context
    request_context.dispose()
    