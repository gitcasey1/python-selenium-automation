# Created by kcfeb at 5/13/2024
Feature: Terms and Conditions

  Scenario: User can open and close Terms and Conditions from sign in page
    # Given Open sign in page (this link https://www.target.com/login is not working)
    Given Open target.com
    When Click Sign In
    When From right side navigation menu, click Sign In
    Given Store original window
    When Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window
    And Switch back to original window