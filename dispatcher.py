from flask import Flask
from flask import render_template
import data
app = Flask(__name__)

@app.route("/authors")
def showAuthors():
    return render_template('authors.html',authors=data.authors)

@app.route("/publications",methods=['GET', 'POST'])
def showPublications():
    return render_template('publications.html',publications = data.publications)


@app.route("/publications/search",methods=['GET', 'POST'])
def searchPublications():
    results = {}
    print request.form
    return render_template('publications.html',publications = data.publications)
	

@app.route("/statistics")
def showStatistics():
    pub_types = {"conference_paper": 0, "book_chapter": 0,"book": 0,"journal":0}
    for publication in data.publications:
	pub_types[data.publications[publication].pub_type] = pub_types[data.publications[publication].pub_type] + 1 
    return render_template('statistics.html',publications = data.publications,authors = data.authors,pub_types=pub_types)

if __name__ == "__main__":
    app.run(debug=True)
