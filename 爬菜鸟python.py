import requests
from bs4 import BeautifulSoup
import xml
def print_txt(url):
	kv={'user-agent':'Mozilla/5.0'}
	            
	req=requests.get(url,headers=kv)
	req.encoding=req.apparent_encoding
	
	bf=BeautifulSoup(req.text,"lxml")

	texts=bf.find_all("div",class_="design")
	
	a_bf = BeautifulSoup(str(texts))
	h2=a_bf.find_all('a',target="_top")
	for k in h2:
		print(k.text)
if __name__ == '__main__':
	
	url="http://www.runoob.com/python3/python3-tutorial.html"
	print_txt(url)
	