import random
from random import randint
import json
import linecache
#from faker import Faker

#Faker.seed(0)

model = linecache.getline("conf.py", 1)
pk = 1
book_line = randint(0, 5)

book_title = linecache.getline('books.txt', book_line)

year = randint(1900, 2000)
pages = randint(1, 300)
rating = random.uniform(0.0, 5.1)
price = random.uniform(1.0, 25.6)
isbn13 = '13-32' #Faker.isbn13()
author = 'John Pupkin' #Faker.name()


def main():
    dictionary = {"model": model,
                  "pk": pk,
                  "fields": {
                      "title": book_title,
                      "year": year,
                      "pages": pages,
                      "isbn13": isbn13,
                      "rating": rating,
                      "price": price,
                      "author": author
                  }
                  }
    c = 0
    jsonString = json.dumps(dictionary, ensure_ascii=False, indent= 4)
    jsonFile = open("data.json", "w")
    jsonFile.write("\n" * c)
    jsonFile.write(jsonString)
    jsonFile.close()
    c += 14
    print(k)



if __name__ == "__main__":
    k = 0
    while k < 100:
        main()
        k += 1

