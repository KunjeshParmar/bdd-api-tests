Feature: Delete user using Reqres API

  Scenario: Successfully delete user with ID 2
    Given the Reqres API is available
    When I send a delete request for user with ID 2
    Then the response status should be 204
