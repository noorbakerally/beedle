class Author:
    def __init__(self,name,co_author = None):
            self.name = name
            self.co_authors = {}
            self.books = []
            self.articles = []

    def addAuthor(self,name):
        if name not in self.co_author:
            self.co_author.append(name)

    def addCoAuthors(self,co_authors):
        self.co_authors = dict(self.co_authors.items() + co_authors.items())
        del self.co_authors[self.name]


class Book:
    def __init__(self,title,year,isbn,publisher,authors=None):
            self.title = title
            self.year = year
            self.isbn = isbn
            self.publisher = publisher
            self.authors = []

    def addAuthor(self,name):
        if name not in self.authors:
            self.authors.append(name)

class Article:
    def __init__(self,title,year,authors=None):
            self.title = title
            self.year = year
            self.authors = []

    def addAuthor(self,name):
        if name not in self.authors:
            self.authors.append(name)
