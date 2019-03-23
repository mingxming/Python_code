import requests
import re
def dowm_pic(url):
	response=requests.get(url)
	#a=response.raise_for_status() 这句子干嘛的
	# 获取的文本实际上是图片的二进制文本
	img = response.content
	with open ("%s.jpg"%name,'wb') as f:   #教训，多看别人的代码，write之前加f...
		f.write(img)    # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
if __name__ == '__main__':    #程序入口，类似于c的main函数
	url = "https://unsplash.com/photos/ydSjTQJYQQk/download"
	name_list=re.split('/',url)   #Split 分割模式，按照你的模式取分割
	name=name_list[-2]    #取列表的最后一个
	dowm_pic(url)
	