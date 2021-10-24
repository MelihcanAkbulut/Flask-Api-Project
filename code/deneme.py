import requests
from bs4 import BeautifulSoup
import json

def checkLink():
    url = "https://bazaar.abuse.ch/export/txt/md5/recent/"
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi,"html.parser")
    allHashes = soup.prettify()
    allMalware = allHashes.split()
    print(allHashes)
    count = (len(allMalware)-37)
    for i in range(len(allMalware)):
        print("{} . dizin  =  {}".format(i,allMalware[i]))

    for i in range(37,count):
        print(allMalware[i])

    print("----------------------")
    for i in range(0,37):
        allMalware.pop(0)
    for i in range(0,5):
        allMalware.pop()

    for i in range(len(allMalware)):
        print(allMalware[i])
def dene():
    url2 = "https://mb-api.abuse.ch/api/v1/"
    myobj = {'query': 'get_info',
             'hash': '1f0a0de6491ff5fb6c2e095a9104777b'}
    rrr = requests.post(url2,myobj)
    responseApi = rrr.text
    information = json.loads(responseApi)
    queryData = information["data"]

    print(queryData)
    print(queryData[0]['sha256_hash'])
    print(queryData[0]['sha1_hash'])
    print(queryData[0]['md5_hash'])
    print(queryData[0]['first_seen'])
    print(queryData[0]['tags'])
    print(queryData[0]['signature'])

checkLink()