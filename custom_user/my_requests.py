import requests

get_url = 'http://127.0.0.1:8001/items/'  # url address to read the phone number from the database


def get_request(data, url=get_url):
    response = requests.get(data, url)
    return response


post_url = 'http://127.0.0.1:8001/create_num/'  # url address to record the phone number in the database


def post_request(data, url=post_url):
    response = requests.post(url, data)
    return response
