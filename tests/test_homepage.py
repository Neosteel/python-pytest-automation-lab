from pages.google_page import GooglePage

def test_homepage_title(page): 
    google_page = GooglePage(page)
    google_page.load()
    assert "Google" in google_page.get_title()

