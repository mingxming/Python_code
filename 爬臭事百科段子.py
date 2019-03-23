from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

def get_url(url):
	kv={'user-agent':'Mozilla/5.0'}
	f = requests.get(url,headers=kv)
	bf=BeautifulSoup(f.content,'lxml')
	bf.encoding=bf.apparent_encoding	
	bcontent=bf.find_all('div',class_='content')
	for k in bcontent:
		print(k.text)
		

	

if __name__ == '__main__':
	url='https://www.qiushibaike.com/text/'
	get_url(url)