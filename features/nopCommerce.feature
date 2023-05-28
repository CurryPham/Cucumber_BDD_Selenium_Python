Feature: OrangeHRM Logo
  Scenario: Logo presence on nopCommerce home Page
    Given launch chrome browser
    When open nopCommerce homepage
    Then verify that the logo present on page
    And close browser