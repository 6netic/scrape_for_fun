import requests
import lxml
from bs4 import BeautifulSoup
from math import ceil


class Book():
	""" This class is about books """

	def __init__(self, urlCat):
		""" Initializing the class """

		self.urlCat = urlCat


	def scrapeUrl(self, url):
		""" This methods counts the number of pages found for this category """

		html = requests.get(url).content
		scraped = BeautifulSoup(html, "lxml")
		
		return scraped


	def categoriesOfBooks(self, scraped):
		""" This method finds all available categories of books on this website """

		catList = []
		categories = scraped.select("li", limit=53)
		# categories of books are ranged from cat[3] to cat[53]
		for i in range(3, 53):	
			catList.append("https://books.toscrape.com/" + categories[i].a['href'])
		
		return catList


	def countPages(self, scraped):
		""" This methods counts the number of pages found for this category """

		pageBooksNumber = scraped.find('form', attrs={'class':'form-horizontal'})
		pageBooksNumber = int(pageBooksNumber.strong.text)
		pageBooksNumber = ceil(pageBooksNumber / 20)
		return pageBooksNumber


	def categoryBooks(self, scraped):
		""" This method finds the category of the books """

		category = scraped.find("h1").text.strip()
		return category


	def getBooks(self, pageBooksNumber, url, category):
		""" This method gives information on a book """

		outputToFile = []
		# Only one page case
		if pageBooksNumber < 2:
			urlModified = url + "index.html"
			# Page des résultats des pages scrapées
			scraped = self.scrapeUrl(urlModified)
			booksUrl = scraped.find_all('h3')	

			outputToFile = self.getInfosOnBooks(booksUrl, category, outputToFile)

		# Several pages case
		else:			
			for i in range(1, pageBooksNumber + 1):
				urlModified = url + "page-{}.html".format(i)
				# Page des résultats des pages scrapées
				scraped = self.scrapeUrl(urlModified)				
				booksUrl = scraped.find_all('h3')
				
				outputToFile = self.getInfosOnBooks(booksUrl, category, outputToFile)

		return outputToFile
		

	def getInfosOnBooks(self, booksUrl, category, outputToFile):
		""" This method gets required information about each book """

		for bookUrl in booksUrl:
			outputToLine = []
			bookUrl = bookUrl.a['href'].replace("../../../", "https://books.toscrape.com/catalogue/")
			scraped = self.scrapeUrl(bookUrl)
			bookDetails = scraped.find_all("td")
			# bookPage
			outputToLine.append(bookUrl)
			# upc
			outputToLine.append(bookDetails[0].text)
			# price_incl_tax
			outputToLine.append((bookDetails[3].text).replace("£", ""))
			# price_excl_tax
			outputToLine.append((bookDetails[2].text).replace("£", ""))
			# book description
			bookDescription = scraped.find_all('p')
			outputToLine.append(bookDescription[3].text)
			# category
			outputToLine.append(category)
			# bookRating
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
			outputToLine.append(bookRating)
			# image url
			imgUrl = scraped.find("img")
			imgUrl = str(imgUrl['src']).replace("../../", "https://books.toscrape.com/")
			outputToLine.append(imgUrl)
			# Concatenating those book infos into general book list
			outputToFile.append(outputToLine)

		return outputToFile















