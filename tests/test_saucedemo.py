import re
from playwright.sync_api import expect

def test_saucedemo_login(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.locator("//input[@id='login-button']").click(timeout=3000)
    expect(page.locator("//span[@data-test='title']")).to_have_text("Products")
    