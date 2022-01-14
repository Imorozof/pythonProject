import requests
import json

url_param = "https://represtapi.absolutins.ru/ords/rest/oauth/token"
header_params = {
    'grant_type': 'client_credentials',
    'Authorization': 'Basic eE15OFdZOFliemFzTUJtZjJDQ0E4US4uOldRSHdXV0RfQ2VIdGdQTEZsWTcxMWcuLg==',
    'Accept':'*/*',
    'Content-Type':'application/x-www-form-urlencoded'
    }
body_params = {
    'grant_type':'client_credentials'
    }
response = requests.post(
    url_param,
    headers=header_params
)
result = response.json()
query = result['query']
data = result['data']
print(query)
print('======================')
print(data)
