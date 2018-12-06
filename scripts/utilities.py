import requests
import json

from scripts.models import UsersRequest


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


def get_all_users(token):
    users = []
    start = 1
    num = 50
    while True:
        users_request = get_users(token, start, num)
        start = start + num
        users.extend(users_request.users)
        if users_request.nextStart == -1:
            break

    return users


def get_users(token, start, num):
    url = 'https://timmons-group.maps.arcgis.com/sharing/portals/self/users'
    params = dict(
        start=start,
        num=num,
        sortField='fullName',
        sortOrder='asc',
        f='json',
        token=token
    )

    resp = requests.get(url=url, params=params)
    data = resp.json()
    print(data)
    return UsersRequest(data)