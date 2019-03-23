from bs4 import BeautifulSoup
from lxml import html
import xml
import requests, json

def get_url(url):
	kv={'user-agent':'Mozilla/5.0'}
	f = requests.get(url,headers=kv)
	bf=BeautifulSoup(f.content,'lxml')
	bf.encoding=bf.apparent_encoding	
	
	print(bf.text)
	

if __name__ == '__main__':
	url='https://www.qiushibaike.com/text/'
	get_url(url)