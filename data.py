import xml.dom.minidom
from classes import Author,Publication

authors = {}
publications_mapping = {"inproceedings":"conference_paper","incollection":"book_chapter","book":"book","article":"journal"}
publications = {}

doc = xml.dom.minidom.parse("/home/noor/temp/gitapps/beedle/smallTree.xml")

#creating all authors in one go
for node in doc.getElementsByTagName("author"):
    author_name = node.childNodes[0].data
    authors[author_name] = Author(author_name)


for node in doc.getElementsByTagName("dblp")[0].childNodes:
    if node.nodeType == 1: #compare element nodes
        title = node.getElementsByTagName("title")[0].childNodes[0].data
        year = node.getElementsByTagName("year")[0].childNodes[0].data
        
        current_authors = {}
        
        #getting the authors for this publications
        for nodeAuthor in node.getElementsByTagName("author"):
            current_author = authors[nodeAuthor.childNodes[0].data]
            current_authors[current_author.name] = current_author
        
        
        #adding the pulication authors
        publications[title] = Publication(title,year,publications_mapping[node.nodeName])
        publications[title].authors = current_authors
        
        #adding the co-authors
        for co_author in current_authors:
            current_authors[co_author].publications[publications_mapping[node.nodeName]].append(publications[title])
            current_authors[co_author].addCoAuthors(current_authors)
