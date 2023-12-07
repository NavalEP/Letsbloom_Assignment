from books.models import Book
import datetime
import random

def randomDate():
    initDate = datetime.datetime(1970, 1, 1)
    finalDate = datetime.datetime(2024, 1, 1)
    sec = random.randint(0, int((finalDate-initDate).total_seconds()))
    ret = initDate+datetime.timedelta(seconds=sec)
    return ret

def mockData(num):
    for i in range(num):
        book = Book(title='Mock Book '+str(i), author='Mock author '+str(i), published_date=randomDate())
        book.save()

if __name__ == '__main__':
    mockData()