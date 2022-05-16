

def before_tag(context, tag):
    if tag == 'create_employee':
        context.execute_steps(u"""
            Given I have data from an new employee
            When I send this data to "users" for register
            Then the employee data should be returned as response""")