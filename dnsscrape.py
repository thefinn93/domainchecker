#!/usr/bin/env python

import sys

import dns.resolver, dns.reversename
import netaddr
import time


def ptr(ip):
    address = dns.reversename.from_address(ip)
    return dns.resolver.query(address, "PTR")[0]

diffs = []
totalstart = time.time()
totalreqs = 0
for subnet in sys.argv[1:]:
    for addr in netaddr.IPNetwork(subnet):
        starttime = time.time()
        try:
            print "%s,%s" % (addr, ptr(str(addr)))
            diffs.append(time.time()-starttime)
        except dns.resolver.NXDOMAIN, dns.resolver.NoNameservers:
            continue

        totalreqs += 1
        if (totalreqs % 10) == 0:
            avg = (sum(diffs)/len(diffs))
            total = time.time() - totalstart
            sys.stderr.write("Average: %s\tTotal: %s\tRequests: %i\n" % (avg, total, totalreqs))
