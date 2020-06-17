import requests
import json

root_url = 'http://127.0.0.1:5000/'

url =  root_url + 'xyz'

d = {'client_name':'Ashwin'}

x = requests.get(url,data=d)

print(x.json())

