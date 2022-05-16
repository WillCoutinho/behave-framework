import requests


class Requests:
    
    def post_request(self, req_url, req_header, body_content):
        try:
            response = requests.post(url=req_url, headers=req_header, data=body_content)
            
        except Exception as e:
            raise f"[SERVICE][POST] Request failed: {e}"
        
        return response

    def put_request(self, req_url, req_header, body_content):
        try:
            response = requests.put(url=req_url, headers=req_header, data=body_content)
    
        except Exception as e:
            raise f"[SERVICE][PUT] Request failed: {e}"
    
        return response

    def get_request(self, req_url, req_header):
        try:
            response = requests.get(url=req_url, headers=req_header)
    
        except Exception as e:
            raise f"[SERVICE][GET] Request failed: {e}"
    
        return response

    def delete_request(self, req_url, req_header):
        try:
            response = requests.delete(url=req_url, headers=req_header)
    
        except Exception as e:
            raise f"[SERVICE][DELETE] Request failed: {e}"
    
        return response

    def patch_request(self, req_url, req_header, req_body):
        try:
            response = requests.delete(url=req_url, headers=req_header, data=req_body)
    
        except Exception as e:
            raise f"[SERVICE][PATCH] Request failed: {e}"
    
        return response
