import requests
import os
import argparse
from dotenv import load_dotenv


red = '\x1b[1;31m'
green = '\x1b[1;32m'
yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
pink = '\x1b[1;35m'
white = '\x1b[1;37m'

avaliable_record_types = {
    'a': 'ip',
    'ns': 'nameserver',
    'mx': 'host'
}


def request_info(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def print_domain_history(domain_history, field):
    for records in domain_history['records']:
        for record in records['values']:
            ip = record[field]
            print(green+'A:', blue+ip, '  ', white+records['first_seen']+'\x1b[0m', '--->', white+records['last_seen']+'\x1b[0m', '  ', yellow+records['organizations'][0]+'\x1b[0m')
        print()


def main():
    load_dotenv()
    api_key = os.environ.get('API_KEY_REGRU')

    headers = {
        "accept": "application/json",
        "APIKEY": api_key
    }

    parser = argparse.ArgumentParser(description='Скрипт запрашивает историю домена с securitytrails.com')
    parser.add_argument('domain', type=str, help='Домен')
    parser.add_argument('record_type', type=str, nargs='?', default='a', help='Тип записи')

    domain = parser.parse_args().domain
    record_type = parser.parse_args().record_type
    url = f'https://api.securitytrails.com/v1/history/{domain}/dns/{record_type}'

    if record_type in avaliable_record_types.keys():
        try:
            domain_history = request_info(url=url, headers=headers)
            field = avaliable_record_types[record_type]
            print_domain_history(domain_history=domain_history, field=field)
        except requests.exceptions.HTTPError as error:
            print(red+'Что-то пошло не так:'+'\x1b[0m')
            print(error)
    else:
        print('Данный тип записи не поддерживается.')


if __name__ == '__main__':
    main()
