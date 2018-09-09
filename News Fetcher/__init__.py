from newsme.nm import NewsMe
from flask import Flask, redirect, url_for, request, render_template
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/search', methods =['POST'])
def search():
	search = request.form['search']
	msg=""
	if search == "":
		return render_template('index.html')
	else:
		match = re.search(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)',search)
		if match:			
			N = NewsMe(search)
			headline = []
			links = []
			for i in N.headlines():
				headline.append(i[0])
				links.append(i[1])
				
			new_match = re.search(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)',links[1])
			if new_match:
				new=""
			else:
				if search[-1]== "/":
    					new=search[0:-1]
				else:
					new=search

			return render_template('search.html',headline=headline,links=links,search=search,new=new)
		else:
			msg = "Enter valid Url"
			return render_template("index.html",msg=msg) 

if __name__ == '__main__':
   app.run(debug = True)