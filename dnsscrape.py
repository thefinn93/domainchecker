#!/usr/bin/env python

import sys

import dns.resolver, dns.reversename
import netaddr


def ptr(ip):
    address = dns.reversename.from_address(ip)
    return dns.resolver.query(address, "PTR")[0]

for subnet in sys.argv[1:]:
    for addr in netaddr.IPNetwork(subnet):
        try:
            print ptr(str(addr))
        except dns.resolver.NXDOMAIN:
            continue
