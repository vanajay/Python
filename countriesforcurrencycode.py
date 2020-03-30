import requests
ccode="http://restcountries.eu/rest/v2/currency/cop"
resp=requests.get(ccode)
if resp.status_code==200:
    #currencycodes=requests.get(ccode)
    #print(type(currencycodes))
    details=resp.json()
    for c in details:
        print(c['name'],c['currencies'])
