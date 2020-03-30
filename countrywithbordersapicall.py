import requests
import sys
import json

fullbordername=[]
url='https://restcountries.eu/rest/v2/all'
borderUrl="https://restcountries.eu/rest/v2/alpha/"
resp=requests.get(url)
#fullBresp=requests.get(fullBorderNames)
if resp.status_code!=200 and fullBorderNames.status_code!=200:
    print("sorry wrong call")
    sys.exit(0)
else:
    items=resp.json()
    for item in items:
        print("{0:20}{1}").format(item['name'].encode('utf-8').strip(), json.dumps(item['borders']),end='')
        boardercodeslist=item['borders']
        #print(type(boardercodeslist))
        for border in boardercodeslist:
            print(border)
            bordernameurl=borderUrl+border
            #print(bordernameurl)
            borderResp=requests.get(bordernameurl)
            #print(type(borderResp))
            borderResponseJson=borderResp.json()
            print(borderResponseJson['name'])
            #fullbordername.append(borderResponseJson['name'])
