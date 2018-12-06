import requests
import json

from scripts.models import UsersRequest, GroupsRequest, ItemsRequest


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
    #print(data)
    return UsersRequest(data)


def get_all_groups(token):
    groups = []
    start = 1
    num = 50
    while True:
        groups_request = get_groups(token, start, num)
        start = start + num
        groups.extend(groups_request.groups)
        if groups_request.nextStart == -1:
            break

    return groups


def get_groups(token, start, num):
    url = 'https://timmons-group.maps.arcgis.com/sharing/rest/community/groups'
    params = dict(
        start=start,
        num=num,
        sortField='title',
        sortOrder='asc',
        f='json',
        q='owner:TimmonsAGOL AND orgid:4fG3YBzBoefRGq66',
        token=token
    )

    resp = requests.get(url=url, params=params)
    data = resp.json()
    print(data)
    return GroupsRequest(data)


def get_all_items(token):
    items = []
    start = 1
    num = 50
    while True:
        items_request = get_items(token, start, num)
        start = start + num
        items.extend(items_request.items)
        if items_request.nextStart == -1:
            break

    return items


def get_items(token, start, num):
    url = 'https://timmons-group.maps.arcgis.com/sharing/rest/search'
    params = dict(
        start=start,
        num=num,
        sortField='title',
        sortOrder='asc',
        f='json',
        q='owner:TimmonsAGOL AND orgid:4fG3YBzBoefRGq66',
        token=token
    )

    resp = requests.get(url=url, params=params)
    data = resp.json()
    print(data)
    return ItemsRequest(data)