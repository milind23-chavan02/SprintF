import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.core import driver

from Utilities.configreader import ConfigReader
from features.pageobjects.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search(BaseSettingsPage):
    def __init__(self, driver):
        super().__init__(driver)

    def text_Searchbar(self, searchTEXT):
        time.sleep(3)
        WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CLASS_NAME, "_3704LK")))

        self.DynamicImplicitWait(40)
        self.TypeEditBox("SEARCHBAR_XPATH", searchTEXT)

    def Click_SEARCHBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SEARCHBUTTON_XPATH")
        time.sleep(5)
    def Check_Relevance(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("RELAVENCE_XPATH")
        time.sleep(5)

    def Check_POPULARITY(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("POPULARITY_XPATH")
        time.sleep(5)

    def Check_LOWTOHIGH(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOWTOHIGH_XPATH")
        time.sleep(5)

    def Check_HIGHTOLOW(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("HIGHTOLOW_XPATH")
        time.sleep(5)

    def Check_NEWESTFIRST(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("NEWESTFIRST_XPATH")
        time.sleep(5)

    def ValidFilter(self, expectedtext):
        self.DynamicImplicitWait(40)
        self.AssertText("filter_XPATH", expectedtext)
        time.sleep(5)

    def minFun(self):
        self.DynamicImplicitWait(40)
        drop = Select(self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[1]/div/div/div/section[7]/div[4]/div[1]/select"))
        drop.select_by_index(1)
        time.sleep(3)
        drop = Select(self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[1]/div/div/div/section[7]/div[4]/div[3]/select"))
        drop.select_by_index(1)
        time.sleep(5)

    def GO(self):
        self.DynamicImplicitWait(40)
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(5)
    def assured(self):
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("check_XPATH")
        time.sleep(5)
    def rating(self):
        self.DynamicImplicitWait(40)
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "div[title='4★ & above']").click()
        time.sleep(20)
        self.driver.find_element(By.CSS_SELECTOR, "div[title='3★ & above']").click()
        time.sleep(20)
        self.driver.find_element(By.XPATH, "(//div[@class='_24_Dny'])[3]").click()
        time.sleep(20)
        self.driver.find_element(By.XPATH, "(//div[@class='_24_Dny'])[4]").click()
        time.sleep(20)

    def brand(self):
        self.DynamicImplicitWait(40)
        self.driver.execute_script("window.scrollBy(0,600)")
        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='ttx38n'])[4]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[1]/div/div/div/section[8]/div[2]/div[1]/div[2]/div/label/div[1]").click()
        time.sleep(10)

    def nextImg(self):
        self.DynamicImplicitWait(40)
        self.driver.find_element(By.XPATH,"//*[ @ id = 'container']/div/div[3]/div/div[2]/div[2]/div/div[1]/div/a/div[1]/div/div/div/img").click()
        time.sleep(10)
