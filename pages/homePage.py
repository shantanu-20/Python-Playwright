from playwright.sync_api import Page, expect

class HomePage:

    def __init__(self, page:Page):
        self.page = page
        self.backpack = page.locator("//a[@id='item_4_title_link']")
        self.bikeLight = page.locator("//a[@id='item_0_title_link']")
        self.itemPrice = page.locator("//div[@data-test='inventory-item-price']")
        self.backToProducts = page.locator("//button[@data-test='back-to-products']")
        self.title = page.locator("//span[@data-test='title']")

    def check_title(self, titleText: str):
        expect(self.title).to_have_text(titleText)

    def click_backpack(self):
        self.backpack.click()
    
    def click_bikeLight(self):
        self.bikeLight.click()

    def click_backToProducts(self):
        self.backToProducts.click()

    def checkPrice(self, price:str):
        expect(self.itemPrice).to_have_text(price)