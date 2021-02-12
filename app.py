import os
import time
import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  


def webscrape():

	path = os.environ['PATH_CHROMEDRIVER']

	chrome_options = Options()  
	chrome_options.add_argument("--headless") #headless browsing

	#updates the driver object
	driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

	driver.get('https://pogoapi.net/Is_It_Shiny/') #async

	time.sleep(1) #forces 1-second wait for driver.get to complete
		
	html_rendered = driver.page_source #page source sould be rendered by now

	#Beautiful Soup: Build a Web Scraper With Python https://realpython.com/beautiful-soup-web-scraper-python/
	soup = BeautifulSoup(html_rendered, 'html.parser') 
	results = soup.find(id='pokemonList') # pull out html for pokemonList id that lists all pokemon currently in the game and their shiny status

	
	#	print("this is results: ", results.prettify()) # nicely format with .prettify() dataquest.io/blog/web-scraping-tutorial-python/
	#extract the text of all <td> tags within results "Finding all instances of a tag at once" dataquest.io/blog/web-scraping-tutorial-python/
	# Beautifulsoup loop through HTML https://stackoverflow.com/questions/38519975/beautifulsoup-loop-through-html

	td_tags = results.find_all('td')

	list_pokemon_and_shiny_status = []

	for td_tag in td_tags:
	
		#"Once we’ve isolated the tag, we can use the get_text method to extract all of the text inside the tag" dataquest.io/blog/web-scraping-tutorial-python/

		#The strip() method returns a copy of the string with both leading and trailing characters removed (based on the string argument passed).
		#e.g. empty spaces
		#https://towardsdatascience.com/top-5-beautiful-soup-functions-7bfe5a693482#:~:text=One%20of%20them%20is%20Beautiful,order%20to%20get%20data%20easily.&text=The%20basic%20process%20goes%20something,it%20any%20way%20you%20want.
		list_pokemon_and_shiny_status.append(td_tag.get_text().strip())


	dict_pokemon_shinystatus = {}

	#slice list for pokemon names https://www.xspdf.com/resolution/52771228.html
	pokemon_list = list_pokemon_and_shiny_status[1::3]

	#slice list for shiny status
	shiny_status = list_pokemon_and_shiny_status[2::3]

	## Merge the two lists to create a dictionary
	#https://thispointer.com/python-6-different-ways-to-create-dictionaries/
	dict_pokemon_shinystatus = dict(zip(pokemon_list, shiny_status))

	print(dict_pokemon_shinystatus)


def getPokemonList():



	print("next steps...")


webscrape()
getPokemonList()

