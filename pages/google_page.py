from pages.base_page import BasePage

class GooglePage(BasePage):
    URL = ("https://www.google.com")

    def load(self):
        self.open(self.URL)


