import requests
from bs4 import BeautifulSoup
import xml
def print_txt(url):
	req=requests.get(url)
	#req.encoding=req.apparent_encoding
	html=req.text
	bf=BeautifulSoup(html,"xml")

	texts=bf.find_all("div",class_="content ")
	a_bf = BeautifulSoup(str(texts))
	h2=a_bf.find_all('h2')
	for k in h2:
		print(k.text)
if __name__ == '__main__':
	
	url="http://mebook.cc/"
	print_txt(url)
	