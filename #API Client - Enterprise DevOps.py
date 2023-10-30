#API Client - Enterprise DevOps 

import requests

ip_address  = input("Please enter you IP Address: ")

url = f"http://ipwho.is/{ip_address}"

get = requests.get(url)

if get.status_code == 200:
    data = get.json()
    print(data)
else:
    print(f"Error: {get.status_code}")
