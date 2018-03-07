"""
Making a HTTP request from python using the urllib package.

See https://docs.python.org/3.5/library/urllib.request.html
For read(), see https://docs.python.org/3.3/tutorial/inputoutput.html#methods-of-file-objects
"""

import urllib.request

u = urllib.request.urlopen("http://www.uis.no/")

# u can be read as a file

# Read the entire page
print (u.read())

# Alternatively: read it line-by-line
# for line in u:
#     print(line)
