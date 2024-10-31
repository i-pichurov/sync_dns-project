import dns.resolver
import socket
from sync_dns.get_ns import get_ns_servers


def add_node(ns_server, record_name, record_type, record_value):
    return {
        'ns_server': ns_server,
        'dns_record': {
            'record_name': record_name,
            'record_type': record_type,
            'record_value': str(record_value).strip('"')
        }
    }


def get_dns_records(domain, record_type, record_name):
    result = []
    ns_servers = get_ns_servers(domain)

    for ns_server in ns_servers:
        
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = [socket.gethostbyname(ns_server)]
            answers = resolver.resolve(record_name, record_type)

            for record_value in answers:
                result.append(add_node(ns_server, record_name, record_type, record_value))

        except Exception as e:
            print(f'An error occurred while querying'
                  f'DNS record on NS server {ns_server}: {e}')
            
    return result