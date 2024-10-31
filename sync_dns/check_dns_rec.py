import dns.resolver
import socket
from sync_dns.get_ns import get_ns_servers


def query_dns_record(domain, record_type, record_name):

    ns_servers = get_ns_servers(domain)

    for ns_server in ns_servers:

        try:

            resolver = dns.resolver.Resolver()
            resolver.nameservers = [socket.gethostbyname(ns_server)]
            answers = resolver.resolve(record_name, record_type)

            for rdata in answers:
                print(f'Query result for {record_name} on '
                      f'NS server {ns_server}: {rdata}')
            print("\n")
        except Exception as e:
            print(f'An error occurred while querying'
                  f'DNS record on NS server {ns_server}: {e}')
