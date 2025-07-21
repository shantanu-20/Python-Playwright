from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page:Page):
        self.page = page
        self.username = page.locator("//input[@id='user-name']")
        self.password = page.locator("//input[@id='password']")
        self.loginButton = page.locator("//input[@id='login-button']")
        
    def enter_username(self,username: str):
        self.username.fill(username)

    def enter_password(self,password: str):
        self.password.fill(password)

    def click_Login(self):
        self.loginButton.click()