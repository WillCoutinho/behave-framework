from behave import given, when, then
from hamcrest import assert_that, is_, has_entries, is_not, empty


@given('I have data from an new employee')
def step_impl(context):
    from features.employees.utils.employee_handler import employee_payload
    
    context.employee = employee_payload()


@when('I send this data to "{endpoint}" for register')
def step_impl(context, endpoint):
    from features.employees.page.employees_requests import register_employee
    
    context.register_response = register_employee(endpoint, body=context.employee)
    
    assert_that(context.register_response.status_code, is_(201), "Response should be Success")
    
    
@then('the employee data should be returned as response')
def step_impl(context):
   
    assert_that(context.register_response.json(),
                has_entries({
                    "name": context.employee["name"],
                    "job": context.employee["job"]}),
                "Response should return the same employee data sent previously")


@given('I have an employee already registered')
def step_impl(context):
    assert_that(context.employee, is_not(None), "Employee should not be empty after register")
    
    
@given('I want to change the "{key}"')
def step_impl(context, key):
    
    if key == 'job':
        context.employee['job'] = "new_job_description"
    
    else:
        context.employee['name'] = "new_employee_name"


@when('I send this data to "{endpoint}" for update the register')
def step_impl(context, endpoint):
    from features.employees.page.employees_requests import update_employee
    
    context.update_response = update_employee(endpoint,
                                              body=context.employee,
                                              _id=context.register_response.json()['id'])
    
    assert_that(context.update_response.status_code, is_(200), "Response status should be '200'")


@then('the job description updated should be returned in the response')
def step_impl(context):
    assert_that(context.update_response.json(),
                has_entries({
                    "name": context.employee["name"],
                    "job": context.employee["job"]}),
                "Response should return the employee data updated")


@given('I have the employee id')
def step_impl(context):
    context.employee_id = context.register_response.json()['id']


@when('I send the employee id to "{endpoint}" for delete the register')
def step_impl(context, endpoint):
    from features.employees.page.employees_requests import delete_employee
    
    context.delete_response = delete_employee(endpoint, _id=context.employee_id)
    
    assert_that(context.delete_response.status_code, is_(204), "Response status should be '204'")
    
    
@then('the employee register should be deleted')
def step_impl(context):
    from features.employees.page.employees_requests import get_employee
    
    resp = get_employee('users/id', _id=context.employee_id)
    assert_that(resp.json(), is_(empty()), "Employee data should not be returned by ID when was deleted")


@given('I have an id from an employee list')
def step_impl(context):
    from random import randint
    
    # ID should be between 1 and 12 has mentioned at https://reqres.in/ - List Users
    context.employee_id = str(randint(1, 12))
    

@when('I send request to "{endpoint}" to get the register')
def step_impl(context, endpoint):
    from features.employees.page.employees_requests import get_employee
    
    context.get_response = get_employee(endpoint, _id=context.employee_id)
    
    assert_that(context.get_response.status_code, is_(200), "Response status should be '200'")
    
    
@then('the employee register should be returned')
def step_impl(context):
    assert_that(context.get_response.json()['data']['email'], is_not(empty()),
                "Employee email returned should not be empty")
    
    assert_that(context.get_response.json()['data']['first_name'], is_not(empty()),
                "Employee first_name returned should not be empty")
    
    assert_that(context.get_response.json()['data']['last_name'], is_not(empty()),
                "Employee last_name returned should not be empty")
