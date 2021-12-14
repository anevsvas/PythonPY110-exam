import random
from random import randint
import json
import linecache

# from faker import Faker

# Faker.seed(0)

model = linecache.getline("conf.py", 1)
pk = 1
book_line = randint(0, 5)
book_title = linecache.getline('books.txt', book_line)


def year_gen():
    year = randint(1900, 2000)
    yield year


def pages_gen():
    pages = randint(1, 300)
    yield pages


def rating_gen():
    rating = random.uniform(0.0, 5.1)
    yield rating


def price_gen():
    price = random.uniform(1.0, 25.6)
    yield price


isbn13 = '13-32'  # Faker.isbn13()
author = 'John Pupkin'  # Faker.name()


def book_gen(pk=1):
    while True:
        yield {"model": model,
               "pk": pk,
               "fields": {
                   "title": book_title,
                   "year": year_gen(),
                   "pages": pages_gen(),
                   "isbn13": isbn13,
                   "rating": rating_gen(),
                   "price": price_gen(),
                   "author": author
               }
               }
        pk += 1


list_books = []


def main():
    book_generator = book_gen()

    for _ in range(100):
        list_books.append(next(book_generator))


def _json():
    jsonString = json.dumps(list_books)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()


if __name__ == "__main__":
    main()
    #_json()
    print(list_books)
