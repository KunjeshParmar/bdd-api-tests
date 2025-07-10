Feature: Get single user details from Reqres API

  Scenario: Successfully retrieve details of user with ID 2
    Given the Reqres API is available
    When I request the details of user with ID 2
    Then the response status should be 200
    And the response should contain the first name "Janet"
