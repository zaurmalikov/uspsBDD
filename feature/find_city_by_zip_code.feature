Feature: Find city by zip code functionality
  As a user
  I want to input zip code
  So I can identify related city in USA

  Scenario: Find city by entering zip code
    Given I am on the main page of usps web site
    When I am navigating to the quick tools menu
    And clicking on Look up a zip code icon
    And clicking find cities by zip code
    And entering zip code
    And clicking Find button
    Then relevant city and state name should be displayed

