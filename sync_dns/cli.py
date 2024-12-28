import argparse


def cli():
    parser = argparse.ArgumentParser(
        description='Prints the value of a DNS '
        'record on all NS servers of a domain.'
        'Example: check_dns mail.ru TXT mail.ru'
        '#Result:'
        'ns1.mail.ru. mail.ru TXT _globalsign-domain-verification=n57ZlrTnnCnyCw1NMLRcU6gFwa3ykYc-KMqjCOSAOP'
        'ns1.mail.ru. mail.ru TXT v=spf1 redirect=_spf.mail.ru'
        'ns2.mail.ru. mail.ru TXT v=spf1 redirect=_spf.mail.ru'
        'ns2.mail.ru. mail.ru TXT _globalsign-domain-verification=n57ZlrTnnCnyCw1NMLRcU6gFwa3ykYc-KMqjCOSAOP')
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
