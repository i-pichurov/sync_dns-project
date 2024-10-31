import dns.resolver


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
