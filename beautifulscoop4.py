from bs4 import BeautifulSoup
import requests
import webbrowser
headers = {
    'authority': 'www.google.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

params = (
    ('q', 'python'),
)

response = requests.get('https://www.google.com/search', params=params,headers=headers)
soup=BeautifulSoup(response.text,'html.parser')
links=soup.find_all("div",class_="r")
for link in links:
    href=link.a.get("href")
    if href=="https://www.python.org/":
        newreq=requests.get(href)
        newsoup=BeautifulSoup(newreq.text,"html.parser")
        newww=newsoup.find_all("div",class_="small-widget download-widget")
        for all in newww:
            link=href+all.a.get("href")
            down_res=requests.get(link)
            down_soup=BeautifulSoup(down_res.text,"html.parser")
            findclass=down_soup.find_all("article",class_="text")
            for every in findclass:
                for allitems in (every.find_all("td")):
                    # new=allitems.split(">")
                    title=allitems.string
                    if "Windows x86 executable installer" ==title:
                        link=allitems.a.get("href")
                        webbrowser.open(link)