#!/usr/bin/env python3
import sys
import os
import logging

modulesFolder = "modules/"


logging.basicConfig()

if len(sys.argv) == 1:
    print("Usage: %s <domain>" % sys.argv[0])
    print("\nfor example, %s finn.io" % sys.argv[0])
    sys.exit(1)

domain = sys.argv[1]

sys.path.append(modulesFolder)

modules = []

for module in os.listdir(modulesFolder):
    if module.endswith('.py'):
        try:
            modules.append(__import__(module[:-3]).Module())
        except ImportError as e:
            logging.error(e)

score = 0
results = []
for module in modules:
    try:
        result = module.check(domain)
        score += result['score']
        results.append((module.name, result['score'], result['reason']))
    except Exception as e:
        try:
            logging.exception("Failed to run module %s" % module.name)
        except:
            logging.exception("Failed to run module")

outputmode = "text"

if outputmode == "md":
    print("Check | Score | Comment")
    print("------|-------|--------")
    for module in results:
        print("%s | %s | %s" % module)
    print("**Total** | **%s** |" % score)
else:
    from tabulate import tabulate
    print(tabulate(results, ['Check', 'Score', 'Comment']))
    print("Total: %s" % score)
