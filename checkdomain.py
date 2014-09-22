#!/usr/bin/env python
import sys
import os
import logging

modulesFolder = "modules/"


logging.basicConfig(level=logging.INFO)

if len(sys.argv) == 1:
    print "Usage: %s <domain>" % sys.argv[0]
    print "\nfor example, %s finn.io" % sys.argv[0]
    sys.exit(1)

domain = sys.argv[1]

"""
try:
    import whois
except ImportError:
    print "Failed to import a module. Please install everything from requirements.txt"
    sys.exit(1)
"""

logging.debug("Preparing to import from %s" % modulesFolder)

sys.path.append(modulesFolder)

modules = []

for module in os.listdir(modulesFolder):
    if module.endswith('.py'):
        try:
            logging.debug("Importing %s" % module)
            modules.append(__import__(module[:-3]).Module())
        except ImportError as e:
            logging.error("Failed to load %s" % module)
            logging.error(e)


score = 0
for module in modules:
    logging.debug("Executing %s" % module.name)
    result = module.check(domain)
    score += result['score']
    logging.info("%s: %s (%s)" % (module.name, result['score'], result['reason']))

logging.info("Total: %i" % score)
