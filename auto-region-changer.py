import requests

 
import os
os.system("cls")

token = input("Your token ?: ")
id = input("ID of group ?: ")


url = "https://discord.com/api/v8/channels/"+str(id)+"/call"

urlpub = "https://discord.com/api/v9/channels/"+str(id)+"/messages"

paa = {
    'content': 'By kzxed#0666'
}

headers = {
    'Authorization': str(token)
}

requests.post(urlpub, headers=headers, json=paa)

region = [
    'hongkong',
    'europe',
    'brazil',
    'us-central'
]


while True:
    regionchoisis = random.choice(region)
    payload = {
        'region': str(regionchoisis)
    }

    requests.patch(url, json = payload, headers=headers)
    print("New region: "+str(regionchoisis))
