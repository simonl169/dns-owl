from owl import dns_functions as dns

if __name__ == "__main__":

    # owl.print_owl()
    print(f"{'':#<40}")
    ip = dns.get_current_public_ip()

    dns.update_all_ip(ip)

    print(f"\tAdd some part to update the index.html")

    print(f"\tDone updating, sleep until next CRON schedule...")
