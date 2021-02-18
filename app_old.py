""" P2 de la version2 - App de scrapping """

import requests
from bs4 import BeautifulSoup
from math import ceil


# Choosing one category
url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"

# Choisissons la catégorie Sequential Art
sequentialArtPage = requests.get(url).content
# scraped is a variable that holds the parsed page
scraped = BeautifulSoup(sequentialArtPage, 'html.parser')

pageBooksNumber = scraped.find('form', attrs={'class':'form-horizontal'})
pageBooksNumber = int(pageBooksNumber.strong.text)
pageBooksNumber = ceil(pageBooksNumber / 20)

# Displaying category
category = scraped.find("h1").text.strip()
#print("Catégorie choisie : ", category)

nombre = 0
# Displaying products on the first page
print("Liste des Url des livres")
booksUrl = scraped.find_all('h3')
for bookUrl in booksUrl:
	bookUrl = bookUrl.a['href'].replace("../../../", "https://books.toscrape.com/catalogue/")
	print("Product Page Url: ", bookUrl)
	bookPage = requests.get(bookUrl).content
	scraped = BeautifulSoup(bookPage, 'html.parser')
	# Recherche de l'universal_product_code (upc) et des autres:
	bookDetails = scraped.find_all("td")
	print("Universal Product Code: ", bookDetails[0].text)
	print("Price including Tax: ", bookDetails[3].text)
	print("Price excluding Tax: ", bookDetails[2].text)
	bookDescription = scraped.find_all('p')
	print("Product Description: ", bookDescription[3].text)
	print("Category: ", category)
	# Déterminons le Book Rating :
	bookRating = str(bookDescription[2])
	bookRating = bookRating.strip('<p class="star-rating ')
	if (bookRating.startswith("Five")):
		bookRating = 5
	elif (bookRating.startswith("Four")):
		bookRating = 4
	elif (bookRating.startswith("Three")):
		bookRating = 3
	elif (bookRating.startswith("Two")):
		bookRating = 2
	elif (bookRating.startswith("One")):
		bookRating = 1
	print("Review Rating: ", bookRating)
	# Déterminons l'url de l"image:
	imgUrl = scraped.find("img")
	imgUrl = str(imgUrl['src']).replace("../../", "https://books.toscrape.com/")
	print("Image Url: ", imgUrl)
	print("")
	nombre += 1

# Cas où nous avons plus d'une page de résultats
if pageBooksNumber > 1:
	for i in range (2, pageBooksNumber + 1):
		url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-{}.html".format(i)
		nextPage = requests.get(url).content
		scraped = BeautifulSoup(nextPage, 'html.parser')
		booksUrl = scraped.find_all('h3')
		for bookUrl in booksUrl:
			bookUrl = bookUrl.a['href'].replace("../../../", "https://books.toscrape.com/catalogue/")
			print("Product Page Url: ", bookUrl)
			bookPage = requests.get(bookUrl).content
			scraped = BeautifulSoup(bookPage, 'html.parser')
			# Recherche de l'universal_product_code (upc) et des autres:
			bookDetails = scraped.find_all("td")
			print("Universal Product Code: ", bookDetails[0].text)
			print("Price including Tax: ", bookDetails[3].text)
			print("Price excluding Tax: ", bookDetails[2].text)
			bookDescription = scraped.find_all('p')
			print("Product Description: ", bookDescription[3].text)
			print("Category: ", category)
			# Déterminons le Book Rating :
			bookRating = str(bookDescription[2])
			bookRating = bookRating.strip('<p class="star-rating ')
			if (bookRating.startswith("Five")):
				bookRating = 5
			elif (bookRating.startswith("Four")):
				bookRating = 4
			elif (bookRating.startswith("Three")):
				bookRating = 3
			elif (bookRating.startswith("Two")):
				bookRating = 2
			elif (bookRating.startswith("One")):
				bookRating = 1
			print("Review Rating: ", bookRating)
			# Déterminons l'url de l"image:
			imgUrl = scraped.find("img")
			imgUrl = str(imgUrl['src']).replace("../../", "https://books.toscrape.com/")
			print("Image Url: ", imgUrl)
			print("")
			nombre += 1




print("Nombre de pages: ", pageBooksNumber)
print("Nombre: ", nombre)










'''
for i in range (1,4): #to scrape names of page 1 to 3
    r = requests.get("https://www.bodia.com/spa-members/page/{}".format(i))
    soup = BeautifulSoup(r.text,"html.parser")
    lights = soup.findAll("span",{"class":"light"})
    lights_list = []
    for l in lights[0:]:
        result = l.text.strip()
        lights_list.append(result)

    print(lights_list)
'''
































