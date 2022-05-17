from urllib.parse import urljoin
from support.services import Requests
from support.url_constants import URL_BASE_FORUM
from features.forum.utils.posts_handler import header_payload
import json

header = header_payload()


def create_post(endpoint, body):
    url = urljoin(URL_BASE_FORUM, endpoint)
    
    data = Requests().post_request(req_url=url, req_header=header, body_content=json.dumps(body))
    
    return data


def update_post(endpoint, body, _id):
    endpoint = endpoint.replace('id', _id)
    
    url = urljoin(URL_BASE_FORUM, endpoint)
    
    data = Requests().put_request(req_url=url, req_header=header, body_content=json.dumps(body))
    
    return data


def delete_post(endpoint, _id):
    endpoint = endpoint.replace('id', _id)
    
    url = urljoin(URL_BASE_FORUM, endpoint)
    
    data = Requests().delete_request(req_url=url, req_header=header)
    
    return data


def get_post(endpoint, _id):
    endpoint = endpoint.replace('id', _id)
    
    url = urljoin(URL_BASE_FORUM, endpoint)
    
    data = Requests().get_request(req_url=url, req_header=header)
    
    return data


def get_post_by_path(endpoint):
    url = urljoin(URL_BASE_FORUM, endpoint)
    
    data = Requests().get_request(req_url=url, req_header=header)
    
    return data
