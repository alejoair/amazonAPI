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
		return JsonResponse({"titulo": "SIN ASIN"}, safe=False)
	if query == "ERROR":
		return JsonResponse({"titulo": "ERROR"}, safe=False)

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
	bsr = "Sin Ranking"
	if bsrtag:
		bsr = bsrtag.contents[2]
	else:
		bsr = "Sin Ranking"
	bsr = bsr.replace(" in Clothing, Shoes & Jewelry (","")
	#OBTENER BULLETS--------------------------------
	#-----------------------------------------------

	bulletstag = soup.find(id="feature-bullets")
	leng = len(bulletstag.contents[1])
	lista = bulletstag.contents[1].find_all("li")
	bullet1 = str(bulletstag) + "bullet 1"
	bullet2 = "None"
	if leng == 6 :	
		bullet1 = lista[3].text #6
		bullet2 = lista[4].text
	elif leng == 7 :
		bullet1 = lista[3].text #7
		bullet2 = lista[5].text
	elif leng == 4 :
		bullet1 = lista[3].text #4
		bullet2 = "Sin descripcion"
	else:	
		bullet1 = lista[3].text #otros
		bullet2 = lista[4].text
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