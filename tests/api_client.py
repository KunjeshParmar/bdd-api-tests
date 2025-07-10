import requests

def create_user(base_url, name, job, headers):
    url = f"{base_url}/users"
    payload = {"name": name, "job": job}
    return requests.post(url, json=payload, headers=headers)

def get_users_by_page(base_url, page, headers):
    url = f"{base_url}/users?page={page}"
    response= requests.get(url, headers=headers)
    return response

def get_single_user(base_url, page, headers):
    url = f"{base_url}/users/{page}"
    response= requests.get(url, headers=headers)
    return response
