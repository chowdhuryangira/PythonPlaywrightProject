

def home_is_visible(page):
    """
    Verify that the home page is visible successfully.
    """
    assert page.get_by_text("Home").is_visible(timeout=3000), "Home page is not visible"


    yield page
