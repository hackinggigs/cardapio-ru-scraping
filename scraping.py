# coding: utf-8
from bs4 import BeautifulSoup
import datetime
import json
import re
import requests

url = 'http://ru.ufsc.br/ru/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")    

# Scrapes for date
text = soup.find('p').text  # Title with date is the page's first paragraph 
match = re.search(r'\d{2}.\d{2}.\d{4}', text)
date_end = datetime.datetime.strptime(match.group(), '%d/%m/%Y').date()
match = re.search(r'\d{2}.\d{2}[ ]', text)
date_start_text = match.group()[:-1] + '/' + str(date_end.year)
date = datetime.datetime.strptime(date_start_text, '%d/%m/%Y').date()

# Scrapes for menu
table = soup.find('tbody')
    
# Fills list with values from table
cells = []
for td in table.find_all('td')[6:]:	
    cells.append(td.text)

# Creates main data structure from values in 'cells'
menu = []
daily_menu = {}
for idx, value in enumerate(cells):
	daily_menu = {}
	if (idx%7 == 0):
		daily_menu['basics'] 	= cells[idx+1] + ', ' + cells[idx+2]
		daily_menu['main_dish'] 		= cells[idx+3]
		daily_menu['side_dish'] 		= cells[idx+4]
		daily_menu['salad'] 			= cells[idx+5]
		daily_menu['dessert'] 		= cells[idx+6]
		daily_menu['date']				= str(date)
		menu.append(daily_menu)
		date += datetime.timedelta(days=1)

data = {'menu': menu}

# Saves to JSON
with open('data.json', 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)
