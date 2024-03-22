import dns_functions as dns

if __name__ == "__main__":

    dns.print_owl()
    print(f"{'':#<40}")
    ip = dns.get_current_public_ip()

    dns.update_all_ip(ip)