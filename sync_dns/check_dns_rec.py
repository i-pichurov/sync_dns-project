import dns.resolver
import socket


def get_ns_servers(domain):

    ns_servers = []

    try:
        answers = dns.resolver.resolve(domain, 'NS')
        for rdata in answers:
            ns_servers.append(str(rdata))

    except dns.resolver.NoAnswer:
        print(f'No NS servers found for {domain}')

    except Exception as e:
        print(f'An error occurred while getting NS servers: {e}')

    return ns_servers


def query_dns_record(domain, record_type, record_name):

    ns_servers = get_ns_servers(domain)

    for ns_server in ns_servers:

        try:

            resolver = dns.resolver.Resolver()
            resolver.nameservers = [socket.gethostbyname(ns_server)]
            answers = resolver.resolve(record_name, record_type)

            for rdata in answers:
                print(f'Query result for {record_name}.{domain} on'
                      f'NS server {ns_server}: {rdata}')
            print("\n")
        except Exception as e:
            print(f'An error occurred while querying'
                  f'DNS record on NS server {ns_server}: {e}')
