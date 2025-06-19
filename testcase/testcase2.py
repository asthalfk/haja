import requests
from pprint import pprint

data = {
    "email":"test@airportgap.com",
    "password":"airportgappassword"
        }

def gen():
    gend = requests.post("https://airportgap.com/api/tokens", json=data)
    # pprint(gend.status_code)
    resp = gend.json()['token']
    print(resp)
    return resp


if __name__ == '__main__':
    gen()