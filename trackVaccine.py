import requests
from bs4 import BeautifulSoup

def getdata(url):
    req = requests.get(url)
    return req.text

data = getdata("https://covid-19tracker.milkeninstitute.org/")
searcher = BeautifulSoup(data, 'html.parser')
result = str(searcher.find_all("div", class_="is_h5-2 is_developer w-richtext"))

print("Developer 1 " + result[46:86])
print("Developer 2 " + result[139:226])
print("Developer 3 " + result[279:305])
print("Developer 4 " + result[358:375])
print("Developer 5 " + result[428:437])
print("Developer 6 " + result[490:571])
