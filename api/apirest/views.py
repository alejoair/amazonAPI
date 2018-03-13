from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


import requests as req
import bs4 
import lxml
import json
import re
# Create your views here.

def APIview(request):

	query = request.GET.get("asin") #OBTIENE EL QUERY
	asin = ""
	if query:
		asin = query
	else:
		asin = "B07BC6DPBV" # ASIN POR DEFECTO

	headers = {'Cache-Control': 'no-cache', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
	urlbase = "https://www.amazon.com/dp/"
	urlfull = urlbase+asin

	#---------------------------------------------------
	#----------Hace el Request-----------------------------------------
	respuesta = req.get(urlfull,headers=headers)
	soup = bs4.BeautifulSoup(respuesta.content,"lxml")

	#-------------------------------------------------
	# Obtiene el Titulo
	titulotag = soup.title.text
	titulo = titulotag.replace("Amazon.com: ","")
	titulolimpio = titulo.replace(": Clothing","")

	#Obtiene BSR----------------------------------
	#---------------------------------------------
	bsrtag = soup.find(id="SalesRank")
	if bsrtag:
		bsr = bsrtag.contents[2]
	else:
		bsr = "Sin Ranking"

	#OBTENER BULLETS--------------------------------
	#-----------------------------------------------

	bulletstag = soup.find(id="featurebullets_feature_div")
	leng = len(bulletstag.contents[1])
	bullet1 = "None"
	bullet2 = "None"
	if leng == 6:	
		bullet1 = bulletstag.contents[1].find_all("li")[4].text #Standard
		bullet2 = bulletstag.contents[1].find_all("li")[5].text
	else:
		bullet1 = bulletstag.contents[1].find_all("li")[4].text #Premiun
		bullet2 = bulletstag.contents[1].find_all("li")[6].text
		
	bullet1 = bullet1.replace("\n","")
	bullet1 = bullet1.replace("\t","")
	
	bullet2 = bullet2.replace("\n","")
	bullet2 = bullet2.replace("\t","")

	#-----------------------------------------------------
	#-----Obtener Precio

	preciotag = soup.find(id="priceblock_ourprice")
	precio = preciotag.text

	# Devuelve el archivo JSON--------------------
	#---------------------------------------------
	return JsonResponse({"titulo": titulolimpio,"bsr": bsr,"precio":precio,"bullet 1":bullet1,"bullet 2":bullet2}, safe=False)