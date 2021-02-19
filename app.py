""" Main File of the application """
import csv
from book import Book


# Main Url
rootUrl = "https://books.toscrape.com/index.html"
# Creating the object
bookObject = Book(rootUrl)
scrapedCategories = bookObject.scrapeUrl(rootUrl)
categories = bookObject.categoriesOfBooks(scrapedCategories)

output = []
print("Processing data ... ... ...")

for category in categories:
	urlCat = category
	url = urlCat.replace("index.html", "")

	# Creating instance of Book class
	bookObject = Book(urlCat)
	scrapedCat = bookObject.scrapeUrl(urlCat)

	category = bookObject.categoryBooks(scrapedCat)
	print("Catégorie : ", category)

	nbOfPages = bookObject.countPages(scrapedCat)
	print("Nombre de pages: ", nbOfPages)

	output += bookObject.getBooks(nbOfPages, url, category)

# Writing to CSV file
with open('books.csv', mode='w') as books:
	entry = csv.writer(books, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	entry.writerow(['product_page_url', 'universal_ product_code (upc)', 'title price_including_tax', 
					'price_excluding_tax number_available', 'product_description', 'category',
					'review_rating', 'image_url'])
	entry.writerows(output)


print("End of processing ! - csv file populated")

