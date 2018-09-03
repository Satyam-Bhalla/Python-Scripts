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
		r = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&search='+search+'')
		json_object = r.json()
		url_links = []
		title = []
		para = []
		for i in range(10):
			url_links.append(json_object[3][i])
			title.append(json_object[1][i])
			para.append(json_object[2][i])


		return render_template('search.html',url_links = url_links,title=title,para=para) 

if __name__ == '__main__':
   app.run(debug = True)