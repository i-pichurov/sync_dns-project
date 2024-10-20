#!/usr/bin/env python3
from sync_dns.check_dns_rec import query_dns_record
from sync_dns.cli import cli


def main():
    domain, dns_record_type, dns_record_name = cli()
    query_dns_record(domain, dns_record_type, dns_record_name)


if __name__ == '__main__':
    main()
