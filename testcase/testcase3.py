import requests
from pprint import pprint
from testcase2 import gen
def coba():
    toks = gen()
    reque = requests.get("https://airportgap.com/api/favorites",
                         headers={ 'Authorization' : f'Token {toks}'

    })

    data = reque.json()
    pprint(data)
    spesific = data['data']['id'=='35729']
    assert spesific['attributes']['airport']['city'] == 'Kapuskasing'
    print("assert done")
#     hahdahasd

if __name__ == '__main__':
    coba()