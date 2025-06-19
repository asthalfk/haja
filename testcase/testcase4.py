import requests
from pprint import pprint

def test():
    # resp = requests.get("https://airportgap.com/api/airports")
    resp = requests.get("https://airportgap.com/api/airports/YCB")
    coba = resp.json().get('data')
    pprint(coba)
    type = coba['type']
    print(coba['id'])
    print(type)


if __name__ == '__main__':
    test()
