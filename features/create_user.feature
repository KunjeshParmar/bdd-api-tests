# Created by Kunjesh at 7/05/2025
Feature: Create a new user via API

  Scenario: Successful user creation
    Given the API is up and running
    When I create a user with name "Kunjesh" and job "QA Engineer"
    Then the response status code should be 201
    And the response should contain the name "Kunjesh"

