# coding=utf-8

import dns


if __name__ == '__main__':
    print(help(dns))

    answers = dns.resolver.query('dnspython.org', 'MX')

    for rdata in answers:
        print('Host', rdata.exchange, 'has preference', rdata.preference)
