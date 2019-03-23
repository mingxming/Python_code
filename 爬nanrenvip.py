from bs4 import BeautifulSoup
from lxml import html
import xml
import requests, json

def get_url(url):
	kv={'user-agent':'Mozilla/5.0'}
	f = requests.get(url,headers=kv)
	bf=BeautifulSoup(f.content,'lxml')
	bf.encoding=bf.apparent_encoding	
	no1=bf.find_all('div', class_="list_box")
	bf2=BeautifulSoup(str(no1),'lxml')
	no2=bf2.find_all('span',class_="fh_bt")
	for k in no2:
		print(k.text)
def all_get():
	
	

if __name__ == '__main__':
	url='http://nanrenvip.cc/nvyouku/1-0-0-0-0-0-0.html'
	get_url(url)