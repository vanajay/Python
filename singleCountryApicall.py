import requests
import sys
import json
url='https://restcountries.eu/rest/v2/all'
resp=requests.get(url)
if resp.status_code!=200:
    print("sorry wrong call")
    sys.exit(0)
else:
    items=resp.json()
    #print(type(items))
    for item in items:
        #print("{0:20}{1}").format(n,k)
        #print(item['name'] ,item["borders"])
        #print(type(item))
        #print(item)
        #print(item.keys())
        #print("------")
        print("{0:20}{1}").format(item['name'].encode('utf-8').strip(), json.dumps(item['borders']))
        #print(item['borders'])
        #for key in item.keys():
        #    print()
        #    value=item[key]
        #    print(key,value)
