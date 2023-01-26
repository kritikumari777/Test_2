import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlist = [ ["Product Category", "GST Rate"],
                 ["Mobile", "18%"],
                 ["Shampoo", "28%"]]
t={}
data=[]
c=0

for product in productlist:
    link = product.find("a",{"class":"product-card"}).get('href')
    productlist.append(link)


for link in productlist:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        ProductCategory=hun.get("p",{"class":"product-action__price"}).text.replace('\n',"")
    except:
        ProductCategory = None

    try:
        GSTRate=hun.get("div",{"class":"product-main__description"}).text.replace('\n',"")
    except:
        GSTRate=None

    whisky = {"ProductCategory":ProductCategory,"GSTRate":GSTRate}

    data.append(whisky)
    c=c+1
    print("completed",c)

df = pd.DataFrame(data)

print(df)


