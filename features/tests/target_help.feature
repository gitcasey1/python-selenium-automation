# Created by kcfeb at 5/15/2024
Feature: Target Help page

  Scenario: User can select Help topic
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Delivery & Pickup
    Then Verify Drive Up & Order Pickup page opened