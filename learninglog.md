# Python Pytest Automation Lab - Learning Log

## Date
March 12, 2026

## What I completed
- Created new project folder: `python-pytest-automation-lab`
- Created virtual environment: `qa-venv`
- Activated virtual environment
- Installed:
  - `pytest`
  - `pytest-playwright`
  - `allure-pytest`
- Installed Playwright browsers using:
  - `python -m playwright install`
- Created `pytest.ini`
- Created first test file: `tests/test_homepage.py`
- Ran first Playwright test successfully
- Created `pages/base_page.py`
- Created `pages/google_page.py`
- Refactored test to use Page Object Model
- Fixed import and class naming issues
- Final result: `1 passed`

## Files created so far
- `pytest.ini`
- `tests/test_homepage.py`
- `pages/base_page.py`
- `pages/google_page.py`

## Important things I learned
- Need to activate `qa-venv` before running tests
- `page` fixture comes from `pytest-playwright`
- Python is case-sensitive (`BasePage` is different from `Basepage`)
- `pytest.ini` belongs in the project root
- `BasePage` stores the Playwright `page` object
- `google_page.load()` means run the `load()` method on the page object

## Current working test
```python
from pages.google_page import GooglePage


def test_homepage_title(page):
    google_page = GooglePage(page)
    google_page.load()
    assert "Google" in google_page.get_title()

    Break taken after first passing page-object-based test.

    