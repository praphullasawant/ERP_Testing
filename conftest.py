import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def login(page: Page):
    page.goto("http://localhost:3000/")
    page.get_by_role("textbox", name="Username or email").fill("admin@gmail.com")
    page.get_by_role("textbox", name="Password").fill("admin")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_load_state("networkidle")
    return page
