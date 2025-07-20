import pytest
from playwright.sync_api import sync_playwright

def test_demo_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()
        page.goto("https://demo.automationtesting.in/Index.html")
        
        title = page.title()
        print("Page title:", title)

        # Take a screenshot for visual verification (optional)
        page.screenshot(path="demo.png")

        # Assert the page title
        assert "Index" in title  # Adjust this assertion as needed

        browser.close()
