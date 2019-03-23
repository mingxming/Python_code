# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import xml
def print_txt(url):
	req=requests.get(url)
	#req.encoding=req.apparent_encoding
	html=req.text
	bf=BeautifulSoup(html,"xml")
	texts=bf.find_all("div",class_="text")
'''	
	for k in texts:
		print(k.text)
		with open (r'C:/Users/ming/Desktop/texttext.txt','a',encoding='utf-8',errors='ignore') as f:   #可以传入'a'以追加（append）模式写入。//
			f.write(k.text) 																			#没有文件就自己创建texttext文件
			
'''
if __name__ == '__main__':
	
	url="http://jandan.net/duan/page-90#comments"
	print_txt(url)
	
	#print(texts[0].text.replace('\xa0'*8,'\n\n'))
