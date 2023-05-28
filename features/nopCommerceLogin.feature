Feature: OrangeHRM Logo

  Scenario Outline: Login to nopCommerce with valid parameter
    Given I launch Chrome browser
    When I open nopCommerce home page
    And Enter username "<username>" and "<password>"
    And Click on login button
    Then User must successfully login to the dashboard page
    And close browser

    Examples:
      | username             | password |
      | admin                | admin123 |
      | admin123             | admin    |
      | test                 | test123  |
      | khoapd2000@gmail.com | 123456   |