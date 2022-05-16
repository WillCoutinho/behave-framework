from faker import Faker


def header_payload():
    return {"Content-Type": "application/json"}


def employee_payload():
    fake = Faker()
    
    employee_obj = {
        "name": fake.name(),
        "job": fake.job()
    }
    
    return employee_obj