from playwright.sync_api import expect


def test_register_user(set_up_ecommerce_website):
    page = set_up_ecommerce_website
    # Verify that home page is visible successfully
    assert page.get_by_text("Home").is_visible(timeout=3000)

    # Click on 'Signup / Login' link and wait for navigation
    with page.expect_navigation(timeout=10000):
        page.get_by_text("Signup / Login").click(timeout=5000)

    # Verify 'New User Signup!' is visible
    assert page.get_by_role("heading", name="New User Signup!").is_visible(timeout=3000)

    # Enter name and email address
    page.get_by_placeholder("Name").fill("user1")
    page.get_by_test_id("signup-email").fill("mail2sapachowdhury@gmail.com")

    # Click 'Signup' button and wait for navigation
    with page.expect_navigation(timeout=10000):
        page.get_by_test_id("signup-button").click(timeout=5000)

    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    assert page.get_by_role("heading", name="ENTER ACCOUNT INFORMATION").is_visible(timeout=3000)

    # Fill details: Title, Name, Email, Password, Date of birth
    page.get_by_text("Mrs").click(timeout=5000)
    page.get_by_test_id("password").click(timeout=3000)
    page.get_by_test_id("password").fill("abc123")
    page.get_by_test_id("days").select_option("1")
    page.get_by_test_id("months").select_option("January")
    page.get_by_test_id("years").select_option("1990")

    # Select checkbox 'Sign up for our newsletter!'
    page.get_by_role("checkbox", name="newsletter").check(timeout=3000)

    # Select checkbox 'Receive special offers from our partners!'
    page.locator("//input[@id='optin']").check(timeout=3000)

    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    page.get_by_test_id("first_name").fill("Angira")
    page.get_by_test_id("last_name").fill("Chowdhury")
    page.get_by_test_id("company").fill("Tech Company")


    page.get_by_test_id("address").fill("123 Tech Street")
    page.get_by_test_id("address2").fill("Suite 456")

    page.get_by_test_id("country").select_option("United States")

    page.get_by_test_id("state").fill("California")
    page.get_by_test_id("city").fill("San Francisco")
    page.get_by_test_id("zipcode").fill("94105")

    page.get_by_test_id("mobile_number").fill("1234567890")

    # Click 'Create Account button'
    page.get_by_test_id("create-account").click(timeout=3000)


    # Verify 'ACCOUNT CREATED!' is visible
    assert page.get_by_role("heading", name="ACCOUNT CREATED!").is_visible(timeout=3000)


    # Click 'Continue' button
    page.get_by_test_id("continue-button").click(timeout=3000)


    # Verify that 'Logged in as username' is visible

    assert page.get_by_text(" Logged in as ").is_visible(timeout=3000)


    # Click 'Logout' button
    page.get_by_text("Logout").click(timeout=3000)

    # Verify that 'Login to your account' is visible
    assert page.get_by_text("Login to your account").is_visible(timeout=3000)
