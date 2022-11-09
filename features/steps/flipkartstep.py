import logging
import time

import allure
from allure_commons._allure import severity
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import configreader
from Utilities.LogUtil import Logger

from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Search import Search
log = Logger(__name__, logging.INFO)


@Given(u'we navigate to flipkart homepage')
def step_imp1(context):
    context.reg = LoginPage(context.driver)
    context.reg.open(configreader.ConfigReader("base info", "URL"))
    log.logger.info("Navigate to Flipkart Homepage")
    context.reg.clickclose()
    log.logger.info("Close button clicked")


#@Then(u'we click on close button')
#def step_imp1(context):
#    context.reg.clickclose()
 #   log.logger.info("Close button clicked")


@When(u'we click on the login button')
def step_imp1(context):
    context.reg.clicklogin()
    log.logger.info("Login button clicked")


@Then(u'we type in the "{username}" edit box')
def step_imp1(context, username):
    context.reg.setusername(username)
    log.logger.info("Username field typed")


@Then(u'we type in the "{password}" field')
def step_imp1(context, password):
    context.reg.setpassword(password)
    log.logger.info("Password field typed")


@Then(u'we click on the sign in button')
def step_imp1(context):
    context.reg.clicksignin()
    log.logger.info("Sign IN BUTTON CLICKED")

@then(u'type "{searchTEXT}" in search bar')
def step_impl(context,searchTEXT):
    context.sea = Search(context.driver)
    context.sea.text_Searchbar(searchTEXT)


@then(u'Click on search button')
def step_impl(context):
    context.sea.Click_SEARCHBUTTON()


@then(u'Check on Relevance is clickable')
def step_impl(context):
    context.sea.Check_Relevance()

@then(u'Check on popularity is clickable')
def step_impl(context):
    context.sea.Check_POPULARITY()


@then(u'Check on Price low-high is clickable')
def step_impl(context):
    context.sea.Check_LOWTOHIGH()


@then(u'Check on Price high-low is clickable')
def step_impl(context):
    context.sea.Check_HIGHTOLOW()


@then(u'Check on newest first is clickable')
def step_impl(context):
    context.sea.Check_NEWESTFIRST()

@then(u'we validate for filter text')
def step_impl(context):
    context.sea.ValidFilter("Filters")

@then(u'we select min price')
def step_impl(context):
    context.sea.minFun()

@then(u'open GO links')
def step_impl(context):
    context.sea.GO()

@then(u'click assured checkbox')
def step_impl(context):
    context.sea.assured()

@then(u'Click on rating checkbox 4* above and 3* above')
def step_impl(context):
    context.sea.rating()

@then(u'click on brand option')
def step_impl(context):
    context.sea.brand()

@then(u'click the image')
def step_impl(context):
    context.sea.nextImg()




