#!/ur/bin/env python

import requests

print(requests.__version__)

r = requests.get("https://raw.githubusercontent.com/carrolji/cmput404/master/get_requests.py")

#print(r)
#print(dir(r))
print(r.text)
print(r.status_code)
# print(r.headers)
# print(r.content)