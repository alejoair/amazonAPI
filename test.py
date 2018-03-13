import requests as req
import bs4 
import lxml
import json
import re

headers = {'Cache-Control': 'no-cache', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
urlbase = "https://www.amazon.com/dp/"
urlfull = urlbase+"B07615B62X"
	#--------------------------B07615B62X-------------------------
	#---------------------------------------------------
respuesta = req.get(urlfull,headers=headers)
soup = bs4.BeautifulSoup(respuesta.content,"lxml")
bsrtag = soup.find(id="feature-bullets")


listali = bsrtag.contents[1].find_all("li")
bullet1 = listali[3].text
bullet2 = listali[4].text
print(len(listali))
print(listali)