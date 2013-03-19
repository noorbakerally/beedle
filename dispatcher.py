from flask import Flask
from flask import render_template
import data
app = Flask(__name__)

@app.route("/authors")
def showAuthors():
    return render_template('authors.html',authors=data.authors)

@app.route("/publications")
def showPublications():
    return render_template('publications.html',publications = data.publications)

if __name__ == "__main__":
    app.run(debug=True)
