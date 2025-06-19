from importlib.metadata import requires

import requests
from pprint import pprint
from jsonschema import validate, ValidationError

data = {
    "email":"test@airportgap.com",
    "password":"airportgappassword"
        }

def gen():
    gend = requests.post("https://airportgap.com/api/tokens", json=data)
    # pprint(gend.status_code)
    resp = gend.json()
    # resp1 = gend.json()['token']
    print(resp)
    return resp
#
response1 = gen()
# response1 = {'token': 'D4d44BBxBiQ9PqKKPsmZLy7H'}


schema1 = {
    "type" : "object",
    "properties" :{
        "token":{
            "type" : "string"
        }
    },
    "required": ["token"],
    "additionalProperties": False  # Ini yang penting!
}

def val():
    try :
        validate(instance=response1, schema=schema1)
        print("done")
    except ValidationError as e:
        print("JSON data is invalid:", e.message)

if __name__ == '__main__':
    val()