Feature: OrangeHRM Logo

  Background: Common steps
    Given I launch Chrome browser
    When I open nopCommerce home page
    And Login to nopCommerce
    And Click on login button


  Scenario: Logo presence on nopCommerce home Page
    Then User must successfully login to the dashboard page

  Scenario: Logo presence on nopCommerce home Page
    When navigate to my Account page
    Then verify my Account page

  Scenario: Logo presence on nopCommerce home Page
    Then navigate to my Computer page
    Then verify my Computer page