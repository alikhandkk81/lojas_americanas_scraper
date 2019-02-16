#!/usr/bin/python3

##############################################
#              logas americanas scarper      #
#              Coded By alikhandkk81         #       
#                                            #
##############################################


import requests
from bs4 import BeautifulSoup

record = []
url = "https://www.americanas.com.br/busca/makebook"

req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')

products = soup.find_all("div", {"class": "product-grid-item ColUI-sc-1ey7nd2-0 iJWnKA ViewUI-oocyw8-6 kvewNe"})


for product in products:

	product = products[0].text.replace('\n', '').strip()
	#print(product)

	record.append(product)
with open("mabooks.txt", "a") as file:
	file.write("Macbook")
	file.write('|'.join(record))


	