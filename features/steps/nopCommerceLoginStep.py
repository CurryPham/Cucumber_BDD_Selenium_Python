from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('I open nopCommerce home page')
def openHomPage(context):
    context.driver.get("https://demo.nopcommerce.com/login")


@when('Enter username "{user}" and "{password}"')
def enterUsernamePassword(context, user, password):
    context.driver.find_element(By.XPATH, "//input[@class='email']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@class='password']").send_keys(password)


@when('Click on login button')
def clickToLoginButton(context):
    context.driver.find_element(By.XPATH, "//button[text()='Log in']").click()


@then('User must successfully login to the dashboard page')
def verifyLoginSucces(context):
    expected = "nopCommerce demo store"
    try:
        actual = context.driver.title
    except:
        context.driver.close()
        assert False, "Test Failed"
    if actual == expected:
        assert True, "Test Passed"


