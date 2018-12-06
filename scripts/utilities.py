import requests
import json


def get_token(username, password):
    url = 'https://www.arcgis.com/sharing/generateToken'
    payload = {
        'username': username,
        'password': password,
        'client': 'requestip',
        'f': 'json'
    }

    r = requests.post(url, data=payload)
    token = json.loads(r.text)
    aToken = token['token']
    return aToken


