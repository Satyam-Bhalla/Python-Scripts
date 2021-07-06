import bs4 as bs
from pprint import pprint
import urllib.request

sauce = urllib.request.urlopen('https://www.lpu.in').read()

soup = bs.BeautifulSoup(sauce,'lxml')
print(soup.title.text)



for url in soup.find_all('a'):
    pprint(url.get('href'))
