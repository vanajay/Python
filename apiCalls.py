import requests
import sys
code="vanajay"
resp=requests.get(r'https://api.github.com/users/srikanthpragada')
if resp.status_code != 200:
   print("sorry wrong call")
   sys.exit(0)
else:
   details=resp.json()
   for k,v in details.items():
       print("{0:20}:{1}").format(k,v)

