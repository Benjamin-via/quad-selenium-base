Feature: Make sure that the login feature is working well

  @test-env
  Scenario: Test login success
    Given The site to test
    When I fill the login form with the right user
    Then I am logged in

  Scenario: Test login failure
    Given The site to test
    When I fill the login form with the wrong user
    Then I am not logged in
    And There is an error displayed