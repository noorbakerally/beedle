import xml.dom.minidom
from classes import Author,Book, Article

authors = {}
books = {}
articles= {}

doc = xml.dom.minidom.parse("smallTree.xml")

#creating all authors in one go
for node in doc.getElementsByTagName("author"):
    author_name = node.childNodes[0].data
    authors[author_name] = Author(author_name)

#creating all books in one go
for node in doc.getElementsByTagName("book"):
        title = node.getElementsByTagName("title")[0].childNodes[0].data
        year = node.getElementsByTagName("year")[0].childNodes[0].data
        isbn = node.getElementsByTagName("isbn")[0].childNodes[0].data
        publisher = node.getElementsByTagName("publisher")[0].childNodes[0].data
        
        #creating a reference to the book
        current_authors = {}
        current_book = Book(title,year,isbn,publisher)
        for nodeAuthor in node.getElementsByTagName("author"):
            current_author = authors[nodeAuthor.childNodes[0].data]
            current_authors[current_author.name] = current_author
        #create temp author list 
        
        
        current_book.addAuthor(current_author)
        current_author.books.append(current_book)

    
        #adding the book to the dictionary
        books[title] = current_book
        
        #adding co-authors
        for co_author in current_authors:
            current_authors[co_author].addCoAuthors(current_authors)
            
#creating all articles in one go
for node in doc.getElementsByTagName("article"):
        title = node.getElementsByTagName("title")[0].childNodes[0].data
        year = node.getElementsByTagName("year")[0].childNodes[0].data
        
        #creating a reference to the book
        current_article = Article(title,year)
        current_authors = {}
        for nodeAuthor in node.getElementsByTagName("author"):
            current_author = authors[nodeAuthor.childNodes[0].data]
            current_article.addAuthor(current_author)
            current_author.articles.append(current_article)
            current_author = authors[nodeAuthor.childNodes[0].data]
            current_authors[current_author.name] = current_author
        articles[title] = current_article
        
        #adding co-authors
        for co_author in current_authors:
            current_authors[co_author].addCoAuthors(current_authors)
        

