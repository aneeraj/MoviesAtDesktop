import urllib.request
import json

url = "http://m.ovies.at/app/fetch.php"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
myList = []
myIDList = []
myNameList = []
for ysa in data['result']:
    print(ysa['mvimg'])
    myList.append(str(ysa['mvimg']))
    myIDList.append(ysa['mvid'])
    myNameList.append(str(ysa['mvname']))
print(myList)