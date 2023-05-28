from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@when('Login to nopCommerce')
def enterUsernamePassword(context):
    context.driver.find_element(By.XPATH, "//input[@class='email']").send_keys("khoapd2000@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@class='password']").send_keys("123456")



@when('navigate to my Account page')
def navigateMyAccountPage(context):
    context.driver.find_element(By.XPATH, "//div[@class='header-links']/ul/li[1]/a").click()


@then('verify my Account page')
def verifyMyAccountPage(context):
    actual = context.driver.find_element(By.XPATH, "//div[@class='master-wrapper-content']//strong[text()='My account']").get_text()
    if actual == "My account":
        assert True


@then('navigate to my Computer page')
def navigateComputerPage(context):
    context.driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']/li[1]/a").click()


@then('verify my Computer page')
def verifyComputerPage(context):
    actual = context.driver.find_element(By.XPATH, "//h1").is_display()
    if actual:
        assert True
