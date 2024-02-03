import socket
import re

def check_ipv4_ipv6_support(domain) -> int:
    ipv4 = False
    ipv6 = False
    try:
        ipv4_address = socket.gethostbyname(domain)
        print(f"{domain} supports IPv4. IPv4 Address: {ipv4_address}")
        ipv4 = True
    except socket.error:
        print(f"{domain} does not support IPv4.")
        ipv4 = False
    try:
        ipv6_address = socket.getaddrinfo(domain, None, socket.AF_INET6)
        print(f"{domain} supports IPv6. IPv6 Address: {ipv6_address[0][4][0]}")
        ipv4 = True
    except socket.error:
        print(f"{domain} does not support IPv6.")
        ipv4 = False
    
    # data ipv4: 1, ipv6: 0, n/a: 9
    if ipv4:
        return 1
    elif ipv6:
        return 0
    else:
        return 9

def is_ipv4(address):
    ipv4_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    return bool(ipv4_pattern.match(address))

def is_ipv6(address):
    ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|:((:[0-9a-fA-F]{1,4}){1,7}|:)$')
    return bool(ipv6_pattern.match(address))
