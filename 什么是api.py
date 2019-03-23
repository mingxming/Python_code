import requests, json

def get_url(url):
	kv={'user-agent':'Mozilla/5.0'}
	f = requests.get(url,headers=kv)
	json_obj=f.text
	
	j=json.loads(json_obj)
	print(j['result']['content'])   #字典操作
									#返回的内容是json格式的数据时，那么可以直接使用json()方法返回一个经过json.loads()处理后的对象。
	
if __name__ == '__main__':
	url='https://api.apiopen.top/singlePoetry'   #别人给的端口api，返回的是json格式数据
	get_url(url)