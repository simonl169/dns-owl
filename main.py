# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
import os
import datetime
from subprocess import call


from dns_functions import *

def dns_main():
    print('###############-------------------------------------')
    print(f'Current Time: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    print('Getting current public IP address...')
    public_server_ip = get_current_public_ip()
    print('###############-------------------------------------')
    print('Reading config.json...')
    with open('config.json', 'r') as f:
        data = json.load(f)

    print('###############-------------------------------------')
    for url in data['domains']:
        print(f'\tChecking IP address for domain {url}')
        local_dns_ip, public_dns_ip = resolve_current_server_ip(url)
        print('\tCompare to current public IP address...')

        decide = compare_ip(public_server_ip, public_dns_ip)

        if not decide:
            print('\tDetecting different DNS IP, update needed')
            password = os.environ.get('STRATO_DYNDNS_PASSWORD', 'default')
            update_dns_ip(url, password)
        else:
            print('\tIP has not changed, no further action')

        print('###############-------------------------------------')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('Running DNS Owl\n')
    print(' {o,o}   ')
    print('./)_)')
    print(' ""\n')
    print('by Simon169\n')

    dns_main()

    print('done! Next repetition set by crontab variables!')

