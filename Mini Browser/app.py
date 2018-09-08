from flask import *
import bs4 as bs
import requests
import urllib
app = Flask(__name__)

@app.route('/')
def index():
    form = Markup(get_page())
    return render_template('index.html', form = form)

@app.route('/<string:data>')
def query(data):
    data = request.query_string
    if str(data)[2:4] == 'ie':
        results = get_query(data)
        form = get_page()
        data = [results[0], Markup(form), Markup(results[1][0])]
        return render_template('result.html', data = data)
    elif str(data)[2:3]:
        return get_site(data)

@app.route("/about")
def about():
    return render_template("about.html")

def get_page():
    sauce = urllib.request.urlopen("https://www.google.com").read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    search_form = [form for form in soup.find_all('form') if form.get('action') == '/search']
    return str(search_form[0])

def get_query(data):
    url = 'https://www.google.com/search?' + str(data)[2:len(str(data)) - 1]
    data = requests.get(url)
    soup = bs.BeautifulSoup(data.text, 'lxml')
    results = [Markup(result) for result in soup.find_all('div', {'class' : 'g'})]
    nav = soup.find_all('table', {'id' : 'nav'})
    return [results, nav]

def get_site(data):
    data = str(data)[4:].split('&sa')[0]
    return redirect(data)

if __name__ == '__main__':
    app.run(debug=False)