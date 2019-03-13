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
gitpat = re.compile(".*github", re.DOTALL | re.IGNORECASE)


jsitems = [i for i in items if pat.match(i)]
print("Found {} javascript items".format(len(jsitems)))
js_github_items = [i for i in items if pat.match(i) and gitpat.match(i)]
print("Found {} javascript items mentioning github".\
      format(len(js_github_items)))

header="""
Javascript vulnerabilities subset of CVE List

    https://cve.mitre.org/data/downloads/index.html\n
"""

with open("jsitems.txt", "w") as outfile:
    outfile.write(header + itembreak + "\n")
    for item in jsitems:

        outfile.write(item + itembreak + "\n")

header="""
Javascript vulnerabilities subset of CVE List mentioning github

    https://cve.mitre.org/data/downloads/index.html\n
"""
with open("jsgithub_items.txt", "w") as outfile:
    outfile.write(header + itembreak + "\n")
    for item in js_github_items:

        outfile.write(item + itembreak + "\n")


# All highlights have direct links to GitHub issues

cve_highlights = [
    "CVE-2016-10531",
    "CVE-2016-10537",
    "CVE-2016-10547",
    "CVE-2016-1927",
]

print("\nFound the following CVE items related to JS:")
for item in cve_highlights:
    print(item)

js_comments = """
Comments:

Most of the Javascript vulnerabilities listed in
CVE pertain to issues with browsers instead of issues
with Javascript frameworks, libraries, things you
would see on GitHub, etc. 

XSS in a browser is a problem but it can't be fixed
by updating your JS dependencies. A lot of the vulnerabilities
I did see were related to C/C++ code. I'm going to try
going lower in the stack with Java to see if there's something
there.
"""
print(js_comments)


header="""
Java vulnerabilities subset of CVE List

    https://cve.mitre.org/data/downloads/index.html\n
"""

pat = re.compile(".*java[\s\n\.]", re.DOTALL | re.IGNORECASE)

javaitems = [i for i in items if pat.match(i)]
print("Found {} java items".format(len(javaitems)))

with open("javaitems.txt", "w") as outfile:
    outfile.write(header + itembreak + "\n")
    for item in javaitems:

        outfile.write(item + itembreak + "\n")

java_github_items = [i for i in items if pat.match(i) and gitpat.match(i)]

print("Java items mentioning github: {}".format(len(java_github_items)))

header="""
Java vulnerabilities subset of CVE List with GitHub reference

    https://cve.mitre.org/data/downloads/index.html\n
"""

with open("java_github_items.txt", "w") as outfile:
    outfile.write(header + itembreak + "\n")
    for item in java_github_items:

        outfile.write(item + itembreak + "\n")

