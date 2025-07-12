Feature: Update user using Reqres API

  Scenario: Successfully update user with ID 2
    Given the Reqres API is available
    When I update the user with ID 2 with name "Murari" and job "Developer"
    Then the response status should be 200
    And the response should contain the job "Developer"