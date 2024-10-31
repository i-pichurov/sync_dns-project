#!/usr/bin/env python3
from sync_dns.stylish import stylish_result
from sync_dns.get_dns_rec import get_dns_records
from sync_dns.cli import cli


def main():
    domain, dns_record_type, dns_record_name = cli()
    print(stylish_result(
        get_dns_records(domain, dns_record_type, dns_record_name)))


if __name__ == '__main__':
    main()
