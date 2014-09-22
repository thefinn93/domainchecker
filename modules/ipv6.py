#!/usr/bin/env python
import logging

class Module(object):
    def __init__(self):
        self.name = "IPv6"
        self.dependencies = ["dnspython"]
        self.author = {
          "name": "Finn Herzfeld",
          "email": "finn@finn.io",
          "url": "https://finn.io"
        }

    def check(self, domain):
        import dns.resolver
        score = 0
        reason = ""
        try:
            results = dns.resolver.query(domain, 'AAAA')
            score = 1
            reason = "IPv6 supported"
        except dns.resolver.NoAnswer:
            score = 0
            reason = "IPv6 not supported"
        return {
            "score": score,
            "reason": reason
        }
