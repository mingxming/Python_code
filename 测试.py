import requests
import os
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
cookies = {'cookie':'1'}
url = 'http://jandan.net/duan/page-90#comments'
r = requests.get(url, cookies=cookies,headers=headers)
r.encoding = 'utf-8'
print (r.text)