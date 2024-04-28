# Created by kcfeb at 4/27/2024
Feature: Test functionality

  Scenario: Verify user sees “Your cart is empty” message is shown
    Given Open target.com
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open target.com
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened