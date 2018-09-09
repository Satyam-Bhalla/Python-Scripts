from bs4 import BeautifulSoup
import urllib.request
headers = {}
headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

class NewsMe:
	def __init__(self, url, order=1):
		self.url = url
		self.order = order
		req = urllib.request.Request(self.url,headers=headers)
		resp = urllib.request.urlopen(req)
		scrap_data = BeautifulSoup(resp.read(), "html.parser")
		self.scrap_data = scrap_data

	def html(self):
		return self.scrap_data.prettify()

	def headlines(self):
		d_l = []
		self.head_list = [(i.text,i.get('href')) for i in self.scrap_data.find_all("a")]
		__n = self.__AvgHeadLen()
		for i in self.head_list:
			if len(i[0].strip())>__n:
				d_l.append((i[0].strip(),i[1]))
		return d_l

	def __AvgHeadLen(self):
		total_letter = 0
		for i in self.head_list:
			total_letter = total_letter+len(i[0].strip())
		return int(total_letter//len(self.head_list)*self.order)
