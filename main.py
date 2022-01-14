import requests
import json

response = requests.post("https://represtapi.absolutins.ru/ords/rest/oauth/token")
header_params = {
    'grant_type': 'client_credentials'
    'Authorization': 'OAuth AgAAlkjlkjKAa976ZB-rXh-t-ookfJJcMP979ZU0',
    'Content-Type': 'application/json'
    }
print("response.status_code:\n{}\n\n".format(response.status_code))
print("response.text:\n{}\n\n".format(response.text))