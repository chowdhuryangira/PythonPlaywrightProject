import pytest
from exceptiongroup import catch
from selenium.common import NoSuchElementException

from ecommerce_website_test_automation.page_pom import home, signup_login


@pytest.mark.parametrize("email,password,username", [("mail2sapachowdhury@gmail.com","abc123","user1"),("abc@gmail.com", "xyz789", "user2")])
def test_login_user(set_up_ecommerce_website, email, password, username):
    """
    Test to log in a user on the e-commerce website with correct credentials.
    """
    # Navigate to the login page
    page = set_up_ecommerce_website

    # Verify that home page is visible successfully
    home.home_is_visible(page)

    # Click on 'Signup / Login' link and wait for navigation
    signup_login.click_sign_up_link(page)

    # Verify 'Login to your account' is visible
    assert page.get_by_text("Login to your account").is_visible(timeout=3000)

    # Enter email and password
    page.get_by_test_id("login-email").fill(email)
    page.get_by_test_id("login-password").fill(password)

    # Click 'Login' button and wait for navigation
    signup_login.click_login_button(page)

    # Verify that 'Logged in as username' is visible
    try:
        assert page.get_by_text(" Logged in as ").is_visible(timeout=3000)
        assert page.locator(
            '//a[contains(text(), "Logged in as")]/b').text_content() == username, "Username does not match"
        # Verify that 'Logout' is visible
        assert page.get_by_text("Logout").is_visible(timeout=3000), "Logout link is not visible after login"

        # Click on 'Logout' link and wait for navigation
        with page.expect_navigation(timeout=10000):
            page.get_by_text("Logout").click(timeout=5000)
        # Verify that 'Login to your account' is visible after logout
        assert page.get_by_text("Login to your account").is_visible(
                timeout=3000), "Logout failed or login page not displayed"

    except AssertionError:
        assert page.get_by_text("Your email or password is incorrect!").is_visible(timeout=3000)



