from newsme.nm import NewsMe
from flask import Flask, redirect, url_for, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/search', methods =['POST'])
def search():
	search = request.form['search']
	if search == "":
		return render_template('index.html')
	else:
		N = NewsMe(search)
		headline = []
		links = []
		for i in N.headlines():
			headline.append(i[0])
			links.append(i[1])
		no = len(headline)
		return render_template('search.html',headline=headline,links=links,search=search,no=no) 

if __name__ == '__main__':
   app.run(debug = True)