# Created by kcfeb at 5/5/2024
Feature: Target loop through colors

  Scenario: Verify user can loop through colors of a selected product
    Given Open https://www.target.com/p/A-91511634
    Then Verify that user can select each color that is clicked
