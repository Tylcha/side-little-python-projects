import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")


#burada uzattimda uzattim alttaki daha mantikli
for i in soup.find_all("div",{"class":"lister-item-content"}):
    for a in i("h3",{"class":"lister-item-header"}):
        #print(a.text)
        pass

#kolay yolu
for i in soup.find_all("h3",{"class":"lister-item-header"}):
    #print(i.text)
    pass

#dahada kolay yolu
basliklar_listesi = soup.find_all("h3", {"class" : "lister-item-header"})
ratingler = soup.find_all("div",{"class" : "inline-block ratings-imdb-rating"})

#print(len(basliklar_listesi),len(ratingler))

a = float(input("deger"))

for basliklar_listesi,ratingler in zip(basliklar_listesi,ratingler):
    basliklar_listesi = basliklar_listesi.text
    ratingler = ratingler.text

    basliklar_listesi = basliklar_listesi.strip()
    basliklar_listesi.replace("\n","")

    ratingler = ratingler.strip()
    ratingler = ratingler.replace("\n","")

    #print("Baslik",basliklar_listesi)
    #print("Rating",ratingler)
    #print("******************************")

    if (float(ratingler) > a):
        print("Film ismi:{} Filmin ratingi:{}".format(basliklar_listesi,ratingler))