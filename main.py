import requests
import os
import argparse
from dotenv import load_dotenv


VERSION = 'v1.01'

# кастомизация подсветки
red = '\x1b[1;31m'
green = '\x1b[1;32m'
yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
white = '\x1b[1;37m'

# доступные записи и их соответсвтие ключам в ответе securitytrails.
avaliable_record_types = {
    'a': 'ip',
    'ns': 'nameserver',
    'mx': 'host',
    'txt': 'value'
}


# Функция делает запрос к securitytrails и получает ответ.
def request_info(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


# Функция выводит ответ в консоль.
def print_domain_history(domain_history, field, record_type):
    if domain_history['records']:
        for records in domain_history['records']:
            for record in records['values']:
                print()
                type = record[field]
                if record_type == 'txt':
                    print(green+record_type+':', blue+type, '  ', white+records['first_seen']+'\x1b[0m', '--->', white+records['last_seen'])
                else:
                    print(green+record_type+':', blue+type, '  ', white+records['first_seen']+'\x1b[0m', '--->', white+records['last_seen']+'\x1b[0m', '  ', yellow+records['organizations'][0]+'\x1b[0m')
        print()
    else:
        print('По этому домену информации нет.')


def main():
    load_dotenv()
    api_key = os.environ.get('API_KEY')  # получаем ключ из .env файла.

    headers = {
        "accept": "application/json",
        "APIKEY": api_key
    }

    parser = argparse.ArgumentParser(prog='alias_name', description=f'Script for securitytrails {VERSION}')
    parser.add_argument('domain', type=str, help='Домен (без слэшей и протоколов)')
    parser.add_argument('record_type', type=str, nargs='?', default='a', help='Тип записи (A, NS или MX)')

    domain = parser.parse_args().domain
    record_type = parser.parse_args().record_type
    url = f'https://api.securitytrails.com/v1/history/{domain}/dns/{record_type}'  # Формируем ссылку для запроса.

    if record_type in avaliable_record_types.keys():  # Прежде чем сделать запрос, проверяем, что тип записи поддерживается.
        try:
            domain_history = request_info(url=url, headers=headers)
            field = avaliable_record_types[record_type]
            print_domain_history(domain_history=domain_history, field=field, record_type=record_type)
        except requests.exceptions.HTTPError as error:
            print(red+'Что-то пошло не так:'+'\x1b[0m')
            print(error)
    else:
        print('Данный тип записи не поддерживается.')


if __name__ == '__main__':
    main()
