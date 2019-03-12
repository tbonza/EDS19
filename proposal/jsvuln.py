""" Javascript vulnerabilities. 

Review javascript vulnerabilities in CVE List
  https://cve.mitre.org/data/downloads/index.html
"""
import re

print(__doc__)


itembreak = "======================================================"
with open("allitems.txt", "rb") as infile:
    data = infile.read().decode("utf-8", "ignore")


items = data.split(itembreak)
print("Found {} items".format(len(items)))


pat = re.compile(".*javascript", re.DOTALL | re.IGNORECASE)

jsitems = [i for i in items if pat.match(i)]
print("Found {} javascript items".format(len(jsitems)))

with open("jsitems.txt", "w") as outfile:
    for item in jsitems:

        outfile.write(item + itembreak + "\n")


