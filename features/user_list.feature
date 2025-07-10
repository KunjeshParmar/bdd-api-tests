Feature: Get paginated user list from Reqres API

  Scenario: Successfully retrieve user list for page 2
    Given the Reqres API is available
    When I request the user list for page 2
    Then the response status should be 200
    And the response should contain 6 users
