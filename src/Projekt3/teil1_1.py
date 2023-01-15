import requests

r = requests.get('https://api.ipify.org?format=json')
if r.status_code != 200:
    print('Fehler!')
else:
    json = r.json()
    print(f"Die IP ist: {json['ip']}")
