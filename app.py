""" Main File of the application """
import csv
from book import Book


# Choosing one category
urlCat = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
# Generic url
url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/"
# When we have only one page
#urlCat = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
#url = "https://books.toscrape.com/catalogue/category/books/travel_2/"

print("Processing... ... ...")
# Creating instance of Book class
bookObject = Book(urlCat)
scrapedCat = bookObject.scrapeUrl(urlCat)

category = bookObject.categoryBooks(scrapedCat)
print("La catégorie actuelle est: ", category)

nbOfPages = bookObject.countPages(scrapedCat)
print("Nombre de pages: ", nbOfPages)

output = bookObject.getBooks(nbOfPages, url, category)
print(output)
#print(type(output))
'''
# Writing to CSV file
with open('books.csv', mode='w') as books:
	entry = csv.writer(books, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	entry.writerow(['product_page_url', 'universal_ product_code (upc)', 'title price_including_tax', 
					'price_excluding_tax number_available', 'product_description', 'category',
					'review_rating', 'image_url'])
	entry.writerows(output)
'''

print("Process Finished !")




































