import json
import os

from scripts import utilities


def main():
    if 'AGOL_USERNAME' not in os.environ or "AGOL_PASSWORD" not in os.environ:
        print('AGOL_USERNAME or AGOL_PASSWORD environment variable not set')
        return

    aToken = utilities.get_token(os.environ['AGOL_USERNAME'], os.environ['AGOL_PASSWORD'])

    print(aToken)

    print('getting all users')
    print('completed')

if __name__== "__main__":
    main()