
Feature: Employee Management
  Allow user to create, get, delete and update an employee

  Scenario: Register an employee
    Given I have data from an new employee
    When I send this data to "users" for register
    Then the employee data should be returned as response

  @create_employee
  Scenario: Update job description from employee
    Given I have an employee already registered
    And I want to change the "job"
    When I send this data to "users/id" for update the register
    Then the job description updated should be returned in the response

  @create_employee
  Scenario: Update name from employee
    Given I have an employee already registered
    And I want to change the "name"
    When I send this data to "users/id" for update the register
    Then the job description updated should be returned in the response

  @create_employee
  Scenario: Delete an employee
    Given I have an employee already registered
    And I have the employee id
    When I send the employee id to "users/id" for delete the register
    Then the employee register should be deleted

  Scenario: Get an employee by ID
    Given I have an id from an employee list
    When I send request to "users/id" to get the register
    Then the employee register should be returned