from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

def suggestBook(title):
   book_url = get_book_url(title)
   books = get_related_books(book_url)
   for book in books:
       print(book)

def get_related_books(book_url):
    driver = webdriver.Chrome()
    driver.get(book_url)

    # Explicitly wait for the carousel widget to be present in the DOM
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.CarouselGroup')))

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    related_books = []

    carousel = soup.find('div', attrs={'data-csa-c-slot-id': "rders_enjoyed"})

    if carousel:
        print("Found carousel")

    else:
        print("No carousel")
        return None

    book_cards = carousel.findAll('div', attrs={'class': 'BookCard__title'})

    for card in book_cards:
        related_books.append(card.text)

    driver.quit()
    return related_books

def get_book_url(title):
    # Perform a search on Goodreads
    search_url = 'https://www.goodreads.com/search?q=' + title.replace(" ", "+")
    response = requests.get(search_url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first search result
    first_result = soup.find('a', attrs={'class':'bookTitle'})
    if first_result:
        book_url = first_result['href']
        print(f'Found book: {book_url}')
        return f'https://www.goodreads.com{book_url}'
    else:
        return None

def findBookGenre(title):
    book_url = get_book_url(title)

    response = requests.get(book_url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    genres = soup.findAll('span', attrs={'class':'BookPageMetadataSection__genreButton'})
    for genre in genres:
        print(genre.text)

def main():
    running = True
    while running:
        book_title = input("Enter a book title: ")
        choice = input("1. Search for a book by title\n2. Find the genre of a book\n3. Exit\n")
        if choice == "1":
            suggestBook(book_title)
        elif choice == "2":
           findBookGenre(book_title)
        elif choice == "3":
            running = False

if __name__ == "__main__":
    main()