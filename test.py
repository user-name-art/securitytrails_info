import requests
import sys
import os
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()
api_key = os.environ.get('API_KEY')


red = '\x1b[1;31m'
green = '\x1b[1;32m'
yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
pink = '\x1b[1;35m'
light_blue = '\x1b[1;36m'
white = '\x1b[1;37m'


domain = sys.argv[1]

headers = {
    "accept": "application/json",
    "APIKEY": api_key
}

url_a = f'https://api.securitytrails.com/v1/history/{domain}/dns/a'

response_a = requests.get(url_a, headers=headers)

for record in response_a.json()['records']:
    print(green+'A:', blue+record['values'][0]['ip'], '   ', white+record['first_seen']+'\x1b[0m', '--->', white+record['last_seen']+'\x1b[0m')

print()

url_ns = f'https://api.securitytrails.com/v1/history/{domain}/dns/ns'

response_ns = requests.get(url_ns, headers=headers)

for record in response_ns.json()['records']:
    pprint(record)
    print()
