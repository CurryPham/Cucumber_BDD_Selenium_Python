Feature: OrangeHRM Logo

  Scenario: Login to nopCommerce with valid parameter
    Given I launch Chrome browser
    When I open nopCommerce home page
    And Enter username "khoapd2000@gmail.com" and "123456"
    And Click on login button
    Then User must successfully login to the dashboard page
    And close browser