import requests
import pydig

def get_current_public_ip():
    ip = requests.get('https://ident.me')
    print('My public IP address is: {}'.format(ip.text))
    return ip.text


def resolve_current_server_ip(url):
    resolver = pydig.Resolver(nameservers=['8.8.8.8'])
    local_ip = pydig.query(url, 'A')
    public_ip = resolver.query(url, 'A')
    print(f'\tLocal IP address for {url} is: {local_ip[0]}')
    print(f'\tPublic IP address for {url} is: {public_ip[0]}')
    return local_ip[0], public_ip[0]

def compare_ip(ip1, ip2):
    print('\tComparing addresses:')
    print(f'\tIP address 1: {ip1}')
    print(f'\tIP address 2: {ip2}')
    if ip1 == ip2:
        return True
    else:
        return False

def update_dns_ip(url, password):

    update_url = 'https://dyndns.strato.com/nic/update?hostname=' + url + '&thisipv4=1'
    #print(update_url)
    r = requests.get(update_url, auth=(url, password))
    #print(r.status_code)
    #print(r.headers)
    #print(r.text)
    if 'nochg' in r.text:
        print('\tNo update needed!')
        print(f'\tFeedback from Strato: {r.text}')
    elif 'good' in r.text:
        print('\tSuccess!')
        print(f'\tFeedback from Strato: {r.text}')
    elif 'badauth' in r.text:
        print('\tBadauth!')
        print('\tYou provided a wrong password or the subdomain does not exist')
    elif 'abuse' in r.text:
        print('\tAbuse! You probaby update too often')
        print(f'\tFeedback from Strato: {r.text}')
    else:
        print('\tSome other error')
        print(f'\tFeedback from Strato: {r.text}')



if __name__ == '__main__':

    print('Test')
