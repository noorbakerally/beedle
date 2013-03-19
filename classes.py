class Author:
    def __init__(self,name,co_author = None):
            self.name = name
            self.co_authors = {}
            self.publications = {}
            self.publications = {"conference_paper": [], "book_chapter": [],"book": [],"journal":[]}

    def addAuthor(self,name):
        if name not in self.co_author:
            self.co_author.append(name)

    def addCoAuthors(self,co_authors):
        self.co_authors = dict(self.co_authors.items() + co_authors.items())
        del self.co_authors[self.name]


class Publication:
    def __init__(self,title,year,pub_type,authors=None):
        self.title = title
        self.year = year
        self.authors = authors
        self.pub_type = pub_type
        
    def addAuthor(self,name):
        if name not in self.authors:
            self.authors.append(name)


