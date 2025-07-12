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


def update_user(base_url, user_id, name, job, headers=None):
    url = f"{base_url}/users/{user_id}"
    payload = {
        "name": name,
        "job": job
    }
    response = requests.put(url, json=payload, headers=headers)
    return response

def delete_user(base_url, user_id, headers=None):
    url = f"{base_url}/users/{user_id}"
    response = requests.delete(url, headers=headers)
    return response

