#!/usr/bin/env python
import logging

# TODO: Deal with non-standard imports for a plugin, ie. by allowing them to
# be ignored but give a revelant error message, such as what needs installing

class Module(object):
    """A module that judges the quality of the registrar a domain is registered with"""

    def __init__(self):
        """The __init__ method only needs to define self.name as the name of the
        plugin. More requirements may come later"""
        self.name = "Registrar"
        self.dependencies = ["pythonwhois"]
        self.author = {
          "name": "Finn Herzfeld",
          "email": "finn@finn.io",
          "url": "https://finn.io"
        }

    def check(self, domain):
        import pythonwhois
        """Looks up the whois info for the domain in question and attempts to extract the registrar"""
        query = pythonwhois.get_whois(domain)
        score = 0
        reason = "Registrar could not be determined"
        if "registrar" in query:
            for registrar in query['registrar']:
                if "godaddy" in registrar.lower():
                    score = -2
                    reason = "Registrar, %s, is known to be evil and of low quality. Additionally, their CEO hunts elephants and they support SOPA." % registrar
            if score == 0: # registrar not listed
                reason = "The registrar, %s, is not known to be particularly bad or good. If you feel this is an oversight on our part, feel free to file a bug or pull request" % registrar


        result = {
            "score": score,
            "reason": reason
        }
        return result