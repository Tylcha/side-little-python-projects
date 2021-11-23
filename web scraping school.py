import requests
from bs4 import BeautifulSoup

#url = "https://bandirma.edu.tr/tr/www/Duyuru/Liste?k=-1"

def sayfaicerigi(url):
    response = requests.get(url)
    html_iceigi = response.content
    soup = BeautifulSoup(html_iceigi, "html.parser")
    return soup

def iceriklerigetir(site):
    for i in sayfa.find_all("h4",{"class":"media-heading"}):
        i = i.text
        i = i.strip()
        print(i)
    return ""

for x in range(1,71):
    site = "https://bandirma.edu.tr/tr/www/Duyuru/Liste?b=1&k=-1&s={}"
    site = site.format(x)
    print(site)
    sayfa = sayfaicerigi(site)
    a = iceriklerigetir(sayfa)
    print(a)