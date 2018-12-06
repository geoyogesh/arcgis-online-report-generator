import json
import os

from scripts import utilities


def main():
    if 'AGOL_USERNAME' not in os.environ or "AGOL_PASSWORD" not in os.environ:
        print('AGOL_USERNAME or AGOL_PASSWORD environment variable not set')
        return

    token = utilities.get_token(os.environ['AGOL_USERNAME'], os.environ['AGOL_PASSWORD'])
    print(token)

    print('getting all users')
    users = utilities.get_all_users(token)
    print(users)
    print('getting all groups')
    groups = utilities.get_all_groups(token)
    print(groups)
    print('getting all items')
    items = utilities.get_all_items(token)
    print(items)
    print('completed')

if __name__== "__main__":
    main()