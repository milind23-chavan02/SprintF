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
    log.logger.info("text typed in searchbar")

@then(u'Click on search button')
def step_impl(context):
    context.sea.Click_SEARCHBUTTON()
    log.logger.info("search button clicked")

@then(u'Check on Relevance is clickable')
def step_impl(context):
    context.sea.Check_Relevance()
    log.logger.info("relavance option clicked")
@then(u'Check on popularity is clickable')
def step_impl(context):
    context.sea.Check_POPULARITY()
    log.logger.info("popularity option clicked")

@then(u'Check on Price low-high is clickable')
def step_impl(context):
    context.sea.Check_LOWTOHIGH()
    log.logger.info("price to low option clicked")

@then(u'Check on Price high-low is clickable')
def step_impl(context):
    context.sea.Check_HIGHTOLOW()
    log.logger.info("Price high-low option clicked")

@then(u'Check on newest first is clickable')
def step_impl(context):
    context.sea.Check_NEWESTFIRST()
    log.logger.info("newest first option clicked")
@then(u'we validate for filter text')
def step_impl(context):
    context.sea.ValidFilter("Filters")
    log.logger.info("filters validated")
@then(u'we select min price')
def step_impl(context):
    context.sea.minFun()
    log.logger.info("min option clicked")
@then(u'open GO links')
def step_impl(context):
    context.sea.GO()
    log.logger.info("high option clicked")

@then(u'click assured checkbox')
def step_impl(context):
    context.sea.assured()
    log.logger.info("assured checkbox selected")

@then(u'Click on rating checkbox 4* above and 3* above')
def step_impl(context):
    context.sea.rating()
    log.logger.info("star rating chckbox clicked")
@then(u'click on brand option')
def step_impl(context):
    context.sea.brand()
    log.logger.info("brand checkbox clicked")

@then(u'click the image')
def step_impl(context):
    context.sea.nextImg()
    log.logger.info("image clicked")




