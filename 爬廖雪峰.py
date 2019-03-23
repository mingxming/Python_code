from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
kv={'user-agent':'Mozilla/5.0'}
f = requests.get(url,headers=kv)                 #Get该网页从而获取该html内容
f.encoding=f.apparent_encoding				#编码问题
soup = BeautifulSoup(f.content, "lxml")  #用lxml解析器解析该网页的内容, 好像f.text也是返回的html
div=soup.find_all('div',id='0014316089557264a6b348958f449949df42a6d3a2e542c000')
a_bf=BeautifulSoup(str(div))
a=a_bf.find_all('a',class_='x-wiki-index-item')
for k in a:
	print(k.text)

#content = soup.find_all('div',class_="p12" )   #因为calss和关键字冲突，所以改名class_
