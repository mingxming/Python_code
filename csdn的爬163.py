
import requests
import re
from bs4 import BeautifulSoup
import sys
import json
import os
 
 
def get_song_id(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print('wrong!!!!!!!')
 
    html = r.text
    soup = BeautifulSoup(html,'html.parser')
 
    song = soup.find_all('ul',attrs = {'class':'f-hide'})[0]
 
    all_song_id = re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>',str(song))
 
    print(all_song_id)
    
    return all_song_id
 
def get_hotcontent(url):
 
    song_list = get_song_id(url)
 
    fpath = 'E:/python/网易云音乐热门评论----周杰伦'
    os.makedirs(fpath)
    os.chdir(fpath)
 
    non_bmp_map = dict.fromkeys(range(0x10000,sys.maxunicode + 1),0xfffd)
 
    
    for single_id in song_list:
        get_content_url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=86377c99d2ebe6570c4146676b9cb36d'.format(single_id[0])
 
 
        param = {'params':'h84Z4kuySxni4TTba7U9khiYWVea9p8Gr+Vlh93EjFPNCtBGh+BTr7BMvx1M3a8FQ9X2UW4Pvif5zCy1gxuR+Ap/52ddf+pXrXlpTIrlkJEtnW0VCiBx7wm7UhFC47JUPtMlvsvm0NJZ+E57lBKHkUzuW3j12gWwnB1Qkvmbl3AC9912lUQIeWCyhN+V3n90yD+3jXxQBLQRDxlZIUWx81/UwV0RhY6kfLxIbZPghFI=',
'encSecKey':'526f02ffc615b9d13974e44ac551608e65a6d14b0adcc05d7cbe86c368aebef465e451a6250de12664a6faf585d567b24a9871a282aff757df2983584c7d5db2d12bbebdaa93b20d8fc65a4d0852ad01b0d450b0cf7373b2b5089edcc394d00925fd82a1e7e11e497f6ab9780cc3280ab3328fc4822d925b137d7bc8721d0f75'}
 
 
        header = {'Host':'music.163.com',
'Origin':'http://music.163.com',
'Referer':'http://music.163.com/song?id='.format(single_id[0]),
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
 
    
        try:
            r = requests.post(get_content_url, headers = header, data = param)
        except:
            print('获取评论失败!')
            continue
        data = r.text.translate(non_bmp_map)
        #print(data)
        json_data = json.loads(data)
 
        hotcomment = json_data['hotComments']
 
        print('歌曲：' + str(single_id[1]) + '\n')
 
        Info = []
 
        for i in range(len(hotcomment)):
            user_name = hotcomment[i]['user']['nickname']
            comment = hotcomment[i]['content']
            like_num = hotcomment[i]['likedCount']
 
 
            Info.append([str(i + 1),user_name,like_num,comment])
 
 
            print('No.'+ str(i + 1))
            print('用户名：'+ str(user_name) + '\t' + '点赞：'+ str(like_num))
            print('评论：'+ comment + '\n')
 
        print('........................................................\n\n')
 
        save(fpath,single_id,Info)
        
        
 
def save(fpath,single_id,Info):
    
    final_fpath = fpath + '/' +str(single_id[1]) + '.txt'
 
    with open(final_fpath,'w',encoding = 'utf-8') as f:
 
        f.write('歌曲名称：'+ str(single_id[1]) + '\n\n')
 
        for i in Info:
            f.write('No.'+ str(i[0]) + '\n')
            f.write('用户名：'+ str(i[1]) + '\t' + '点赞：' + str(i[2]) + '\n')
            f.write('评论：'+ str(i[3]) + '\n\n')
 
 
def main():
    url = 'http://music.163.com/artist?id=6452'
    
    get_hotcontent(url)
 
 
main()
