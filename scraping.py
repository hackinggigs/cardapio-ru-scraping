# coding: utf-8
from bs4 import BeautifulSoup
import requests

url = 'http://ru.ufsc.br/ru/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")    

table = soup.find('tbody')
    
cells = []
for td in table.find_all('td')[6:]:
    print(td.text)
    print('---')
    cells.append(td.text)

cardapio = []

cardapio_dia = {}

for idx, value in enumerate(cells):
	cardapio_dia = {}
	if (idx%7 == 0):
		cardapio_dia['acompanhamento'] 	= cells[idx+1] + ', ' + cells[idx+2]
		cardapio_dia['principal'] 		= cells[idx+3]
		cardapio_dia['complemento'] 	= cells[idx+4]
		cardapio_dia['salada'] 			= cells[idx+5]
		cardapio_dia['sobremesa'] 		= cells[idx+6]
		cardapio.append(cardapio_dia)

print('segunda', cardapio[0])
print()
print('terça', cardapio[1])
