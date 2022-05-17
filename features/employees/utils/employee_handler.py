

def header_payload():
    return {"Content-Type": "application/json"}


def employee_payload():
    from faker import Faker
    
    fake = Faker()
    return {
        "name": fake.name(),
        "job": fake.job()
    }