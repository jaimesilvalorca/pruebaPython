import requests
from json import loads, dumps

def get(url, headers = {}, payload = {}):
    return loads(requests.get(url=url, headers=headers, data=dumps(payload)).text)