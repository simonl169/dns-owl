from owl import dns_functions as dns
from owl.config import load_config

if __name__ == "__main__":

    # owl.print_owl()
    print(f"{'':#<40}")

    ip_provider = load_config('./config.json')['PUBLIC_IP_CHECK']

    ip = dns.get_current_public_ip(ip_provider)

    dns.update_all_ip(ip)

    print(f"\tAdd some part to update the index.html")

    print(f"\tDone updating, sleep until next CRON schedule...")
