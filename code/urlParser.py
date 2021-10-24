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
    count = (len(allMalware)-37)
    for i in range(0,37):
        allMalware.pop(0)
    for i in range(0,5):
        allMalware.pop()
    return [count, allMalware]

def checkAllMalware(hash):
    url2 = "https://mb-api.abuse.ch/api/v1/"
    print(hash)
    myobj = {'query': 'get_info',
             'hash': '{}'.format(hash)}
    rrr = requests.post(url2,myobj)
    responseApi = rrr.text
    information = json.loads(responseApi)
    print(information)
    queryData = information["data"]
    return queryData

