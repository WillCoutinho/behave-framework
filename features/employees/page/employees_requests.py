from urllib.parse import urljoin
from support.services import Requests
from support.url_constants import URL_BASE_EMPLOYEE
from features.employees.utils.employee_handler import header_payload
import json

header = header_payload()


def register_employee(endpoint, body):
    url = urljoin(URL_BASE_EMPLOYEE, endpoint)
    
    data = Requests().post_request(req_url=url, req_header=header, body_content=json.dumps(body))
    
    return data


def update_employee(endpoint, body, _id):
    endpoint = endpoint.replace('id', _id)
    
    url = urljoin(URL_BASE_EMPLOYEE, endpoint)
    
    data = Requests().put_request(req_url=url, req_header=header, body_content=json.dumps(body))
    
    return data


def delete_employee(endpoint, _id):
    endpoint = endpoint.replace('id', _id)
    
    url = urljoin(URL_BASE_EMPLOYEE, endpoint)
    
    data = Requests().delete_request(req_url=url, req_header=header)
    
    return data


def get_employee(endpoint, _id):
    endpoint = endpoint.replace('id', _id)
    
    url = urljoin(URL_BASE_EMPLOYEE, endpoint)
    
    data = Requests().get_request(req_url=url, req_header=header)
    
    return data

