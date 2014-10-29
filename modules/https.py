#!/usr/bin/env python3

class Module(object):
    def __init__(self):
        self.name = "HTTPS"
        self.dependencies = ["requests"]
        self.author = {
          "name": "Finn Herzfeld",
          "email": "finn@finn.io",
          "url": "https://finn.io"
        }

    def check(self, domain):
        """Checks if the domains supports https"""
        import requests

        score = 0
        reason = ""
        try:
            requests.get("https://%s" % domain, timeout = 5)
            score = 1
            reason = "HTTPS supported"
        except requests.exceptions.ConnectionError:
            try:
                requests.get("https://www.%s" % domain, timeout = 5)
                score = 1
                reason = "No HTTPS support on the naked domain (%s), but www.%s appears to have it" % (domain, domain)
            except requests.exceptions.ConnectionError:
                score = -1
                reason = "No HTTPS support"
        return {
            "score": score,
            "reason": reason
        }
