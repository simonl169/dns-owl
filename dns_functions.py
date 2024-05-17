import requests
import pydig
import json
from notifications import Notifier
from owl import print_owl
from config import load_config


if load_config('config.json')['ENABLE_NOTIFICATIONS']:
    notification_service = Notifier()
else:
    notification_service = None


def get_current_public_ip() -> str:
    ip_address = requests.get('https://ident.me')
    print(f'\tMy public IP address is: {ip_address.text}')
    return ip_address.text


def resolve_current_server_ip(url, nameservers='8.8.8.8') -> [str, str]:
    nameservers = [nameservers]
    resolver = pydig.Resolver(nameservers=nameservers)
    local_ip = pydig.query(url, 'A')
    public_ip = resolver.query(url, 'A')
    print(f'\tLocal IP address for {url} is: {local_ip[0]}')
    print(f'\tPublic IP address for {url} is: {public_ip[0]}')
    return local_ip[0], public_ip[0]


def compare_ip(ip1, ip2) -> bool:
    print('\tComparing addresses:')
    print(f'\tIP address 1: {ip1}')
    print(f'\tIP address 2: {ip2}')
    if ip1 == ip2:
        return True
    else:
        return False


def set_ip(cloudflare, domain, current_ip: str):
    """
    sets the ip in via cloudflare api
    """
    zone_id = cloudflare['ZONE_ID']
    api_key = cloudflare['API_KEY']
    user_email = cloudflare['USER_EMAIL']

    record_id = domain['RECORD_ID']
    record_name = domain['RECORD_NAME']

    print(f"\tCloudflare Zone ID is: {zone_id}")
    print(f"\tCloudflare API Key is: {api_key}")
    print(f"\tRecord ID is: {record_id}")
    print(f"\tRecord Name is: {record_name}")

    url = (
            "https://api.cloudflare.com/client/v4/zones/%(zone_id)s/dns_records/%(record_id)s"
            % {"zone_id": zone_id, "record_id": record_id}
    )

    headers = {
        "X-Auth-Email": user_email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json",
    }

    payload = {"type": "A", "name": record_name, "content": current_ip}
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    # print(response.status_code)
    # print(response.json()['success'])

    return response


def update_all_ip(current_ip):
    data = load_config('config.json')

    cf = data

    for domain in data['domains']:
        print(f"{'':#<40}")
        print(f"\tPerform Check if Update is necessary...")
        domain_ip = resolve_current_server_ip(domain['RECORD_NAME'])[1]
        check = compare_ip(current_ip, domain_ip)
        if check:
            print(f"\tIP for domain: {domain['RECORD_NAME']} is {domain_ip} which is the current public IP {current_ip}. No Update necessary!")
            if notification_service:
                notification_service.send_success(f"\tIP for domain: {domain['RECORD_NAME']} is {domain_ip} which is the current public IP {current_ip}. No Update necessary!")
        else:
            print(f"\tUpdating DynDNS IP for domain: {domain['RECORD_NAME']}...")
            response = set_ip(cf, domain, current_ip)

            if response.json()['success']:
                print(f"\tIP was set successfully!")
                if notification_service:
                    notification_service.send_success(f"IP for domain {domain} was successfully set to {current_ip}")
            else:
                print(f"\tThere was an error, see below for more details")
                print(f"\tResponse code was: {response.status_code}")
                if notification_service:
                    notification_service.send_error(f"An error occurred, status code {response.status_code}")
                print(f"\tResponse json is: {response.json()}")

    print('\tDone!')
    print(f"{'':#<40}")


if __name__ == '__main__':

    print(f"{'':#<40}")
    ip = get_current_public_ip()

    update_all_ip(ip)

    print(f"\tDone updating, sleep until next CRON schedule...")
