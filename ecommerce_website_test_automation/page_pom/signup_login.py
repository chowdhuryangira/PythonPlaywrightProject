


def click_sign_up_link(page):
    """
    Clicks the 'Signup / Login' button on the e-commerce website.
    """
    with page.expect_navigation(timeout=10000):
        page.get_by_text("Signup / Login").click(timeout=5000)

def fill_signup_details(page, name, email):
    """
    Fills in the signup form with the provided name and email.
    """
    page.get_by_placeholder("Name").fill(name)
    page.get_by_test_id("signup-email").fill(email)


def click_sign_up_button(page):
    """
    Clicks the 'Signup' button and waits for navigation.
    """
    with page.expect_navigation(timeout=10000):
        page.get_by_test_id("signup-button").click(timeout=5000)

def get_new_user_sign_up_locator(page):
    """
    Sets the locator for the 'New User Signup!' heading.
    """
    return page.get_by_role("heading", name="New User Signup!")

def click_login_button(page):
    """
    Clicks the 'Login' button and waits for navigation.
    """
    with page.expect_navigation(timeout=10000):
        page.get_by_test_id("login-button").click(timeout=5000)