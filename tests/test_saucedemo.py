import re
from playwright.sync_api import Page
from pages.homePage import HomePage
from pages.loginPgae import LoginPage

def test_login(page: Page)->None:
    loginPage=LoginPage(page)
    homepage=HomePage(page)
    loginPage.enter_username("standard_user")
    loginPage.enter_password("secret_sauce")
    loginPage.click_Login()
    homepage.check_title("Products")

def test_price(page: Page)->None:
    loginPage=LoginPage(page)
    homepage=HomePage(page)
    loginPage.enter_username("standard_user")
    loginPage.enter_password("secret_sauce")
    loginPage.click_Login()
    homepage.check_title("Products")
    homepage.click_backpack()
    homepage.checkPrice("$29.99")
    homepage.click_backToProducts()
    homepage.click_bikeLight()
    homepage.checkPrice("$9.99")
