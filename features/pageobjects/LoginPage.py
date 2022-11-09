from Utilities import configreader
from features.pageobjects.Base import BaseSettingsPage


class LoginPage(BaseSettingsPage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)
        self.DynamicImplicitWait(40)

    def clickclose(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("close_XPATH")

    def clicklogin(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("login_XPATH")

    def setusername(self, username):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("username_XPATH", username)

    def setpassword(self, password):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("password_XPATH", password)

    def clicksignin(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("submitlogin_XPATH")
