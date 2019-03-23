'''
遇到问题，图片url给加密了
解决方法，找到js中的解密函数，用python模拟js加密方式，拿到加密处理后的数据
参考  http://tendcode.com/article/jiandan-meizi-spider/
'''
import requests
url='http://apps.bdimg.com/libs/jquery/2.0.3/jquery.min.js'
r=requests.get(url)
print(r.text)