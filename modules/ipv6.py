#!/usr/bin/env python3

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
        import socket
        score = 0
        reason = "IPv6 not supported"
        for address in socket.getaddrinfo(domain, 80):
            if address[0] == socket.AF_INET6:
                score = 1
                reason = "IPv6 supported"
        return {
            "score": score,
            "reason": reason
        }
