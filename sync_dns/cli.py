import argparse


def cli():
    parser = argparse.ArgumentParser(
        description='Prints the value of a DNS'
        'record on all NS servers of a domain.')
    parser.add_argument(
        'domain', type=str,
        help='Input domain name')
    parser.add_argument(
        'dns_record_type', type=str,
        help='Input DNS record type')
    parser.add_argument('dns_record_name', type=str,
                        help='Input DNS record name')
    args = parser.parse_args()
    return args.domain, args.dns_record_type, args.dns_record_name
