# Created by kcfeb at 5/4/2024
Feature: Test Target

  Scenario: Verify user sees 10 benefit cells
    Given Open https://www.target.com/circle
    Then Verify there are 10 benefit cells


  Scenario: Verify added product is in cart
    Given Open target.com
    When Search for juice
    When Click Add to cart button
    When From right side navigation menu, click add to cart button
    When From right side navigation menu, click View cart & check out
    Then Verify added product is in the cart