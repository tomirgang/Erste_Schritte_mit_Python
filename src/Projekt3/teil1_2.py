import requests
import sys

r = requests.get('https://api.ipify.org?format=json')
if r.status_code != 200:
    print('Fehler, IP konnte nicht ermittelt werden!')
    sys.exit(1)

json = r.json()
ip = json['ip']
print(f"Die IP ist: {ip}")

geo_url = f'https://ipinfo.io/{ip}/geo'
r = requests.get(geo_url)
if r.status_code != 200:
    print('Fehler, Geo-Daten konnten nicht ermittelt werden!')
    sys.exit(1)

json = r.json()
print(f"Land: {json['country']}\nStadt: {json['city']}\nISP: {json['org']}")
