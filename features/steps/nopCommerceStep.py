from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('open nopCommerce homepage')
def openHomPage(context):
    context.driver.get("https://demo.nopcommerce.com/login")


@then('verify that the logo present on page')
def verifyLogo(context):
    context.driver.find_element(By.XPATH, "//input[@class='email']").send_keys("admin@yourstore.com")
    context.driver.find_element(By.XPATH, "//input[@class='password']").send_keys("admin")
    context.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    actual = context.driver.title
    expected = "nopCommerce demo store"
    if actual == expected:
        assert True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
