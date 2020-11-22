import time

from behave import *
from selenium import webdriver
# Do not remove that import
import chromedriver_binary

use_step_matcher("re")


@given("The site to test")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(2)
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@when("I fill the login form with the right user")
def step_impl(context):
    context.driver.find_element_by_id("txtUsername").send_keys("admin")
    context.driver.find_element_by_id("txtPassword").send_keys("admin123")
    context.driver.find_element_by_id("btnLogin").click()


@then("I am logged in")
def step_impl(context):
    assert context.driver.find_element_by_id('menu_dashboard_index').is_displayed() is True


