

import pytest

@pytest.fixture(scope="session")

def set_up_ecommerce_website(playwright):
    """
    Fixture to set up the Playwright environment for testing.
    This fixture launches a browser, creates a new context and page,
    and navigates to the sign-in page of the e-commerce website.
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state("networkidle", timeout=1000)
    page.goto("https://automationexercise.com/")
    playwright.selectors.set_test_id_attribute("data-qa")
    page.set_default_timeout(5000)

    yield page

    # Cleanup after tests
    context.close()
    browser.close()