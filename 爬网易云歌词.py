import requests, json

def get_url(url):
	kv={'user-agent':'Mozilla/5.0'}
	f = requests.get(url,headers=kv)
	json_obj=f.text
	
	j=json.loads(json_obj)
	print(j['lrc']['lyric'])
	

if __name__ == '__main__':
	url='http://music.163.com/api/song/lyric?id=1336990252&lv=1&kv=1&tv=-1'   #旧端口api
	get_url(url)
 
#遇到问题动态加载网站，返回的数据是json格式，歌词存在一个xml格式的数据里，提交的两个参数还给加密了，要解密。
#http://www.zhouzying.cn/58.html 参考
#