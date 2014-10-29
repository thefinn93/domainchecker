#!/usr/bin/env python
import logging

class Module(object):
    def __init__(self):
        self.name = "www"
        self.dependencies = ["requests"]
        self.author = {
          "name": "Finn Herzfeld",
          "email": "finn@finn.io",
          "url": "https://finn.io"
        }

    def check(self, domain):
        import requests
        from urllib.parse import urlparse

        score = 0
        reason = ""

        nakedreq = requests.get("http://%s" % domain)
        nakedreqURL = urlparse(nakedreq.url)
        wwwreq = requests.get("http://www.%s" % domain)
        wwwreqURL = urlparse(wwwreq.url)


        if nakedreqURL.netloc == domain:
            score = 0
            reason = "Naked domain (%s) does not redirect to www (but www does not redirect to naked)" % domain
            if wwwreqURL.netloc == domain:
                score = 1
                reason = "www.%s redirects to %s" % (domain, domain)
        elif nakedreqURL.netloc == "www.%s" % domain:
            score = -1
            reason = "Naked domain redirects to www."

        return {
            "score": score,
            "reason": reason
        }
