#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
#作者：どうでもいい菌 
#网址：https://space.bilibili.com/450634867

# 爬取所有图片的url
import requests
import datetime
import re
import os
import urllib.request
from urllib.parse import quote
from PIL import Image
from io import BytesIO

name = input('请输入老婆的名称：')
a = input('起始页码：')
p = input('终止页码：')
text = quote(name, 'utf-8')

while True:
    # o_path = input('请输入保存文件地址(E:\编程\python\项目\爬取p站图片\【p站】动漫人物特辑)：')
    o_path = "E:\编程\python\项目\爬取p站图片\【p站】动漫人物特辑"
    if not os.path.exists(o_path):
        print('路径不存在!')
    else :
        os.makedirs(o_path + '\\' + name+'('+a+'-'+p+')'+'页')
        file_path = o_path + '\\' + name+'('+a+'-'+p+')'+'页'
        break
start=datetime.datetime.now()
headers = {
    "cookie": "login_ever=yes; ki_r=; _ga=GA1.3.2013717293.1588508944; _ga=GA1.2.2013717293.1588508944; adr_id=HgGthok6pSrytKARGF4DEHpmUzCpDLr7G0mwm00p9gcnRt3N; _td=a4cb85b7-1b2f-4084-b5fa-8e96bc59d559; BNet=200624; ki_t=1588508857697%3B1593011840128%3B1593011840128%3B11%3B24; _gid=GA1.2.1385331877.1593011840; first_visit_datetime_pc=2020-06-25+00%3A29%3A01; yuid_b=IGdlAHc",  # 根据自己的浏览器情况填写，UA头也是
    "user-agent": "",
    "referer": "https://www.pixiv.net/ajax/search/artworks/"+text+"?word="+text+"&order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh"
}
for url in range(int(a),int(p)+1):
    URL = "https://www.pixiv.net/ajax/search/artworks/" + text + "?word=" + text + "&order=date_d&mode=all&p=" + str(url) + "&s_mode=s_tag&type=all&lang=zh"

    # URL = "https://pixiv.bilibilinet.com/ajax/search/artworks/"+text+"?word="+text+"&order=date_d&mode=all&p="+p+"&s_mode=s_tag&type=all&lang=zh"
#https://i.pximg.net/img-original/img/2011/02/19/07/46/39/16790330_p0.jpg
#https://i.pximg.net/img-master/img/2015/07/10/13/27/51/51341751_p0_master1200.jpg
    session = requests.get(URL, headers=headers)
    JSON = session.json()

    i = 0
    d =  0

    while i < len(JSON["body"]["illustManga"]["data"]):

        ID = JSON["body"]["illustManga"]["data"][i]["id"]
        userId = JSON["body"]["illustManga"]["data"][i]["userId"]
        title = JSON["body"]["illustManga"]["data"][i]["title"]
        userName = JSON["body"]["illustManga"]["data"][i]["userName"]
        url = JSON["body"]["illustManga"]["data"][i]["url"]
        o_url_1 = re.sub('c/250x250_80_a2/img-master', 'img-original', url)
        o_url = re.sub('_square1200', '', o_url_1)
#https://i.pximg.net/c/250x250_80_a2/img-master/img/2013/06/06/00/39/03/36184316_p0_square1200.jpg
#https://i.pximg.net/img-original/img/2011/02/19/07/46/39/16790330_p0.jpg
        print("作品名称：" + title, "作品ID：" + str(ID),  "作者姓名和ID：" + userName, str(userId))
        print(o_url,'Downloading……\n')

        img_url = o_url
        file_name = "作品名称：" + title, "作品ID：" + str(ID)

        try:
            file_suffix = os.path.splitext(img_url)[1]
            filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)

            response = requests.get(img_url, headers=headers)
            image = Image.open(BytesIO(response.content))
            image.save(filename)
        except IOError as e:
            print("IOError")
            d += 1
        except Exception as e:
            print("Exception")
            d += 1
        i += 1

end=datetime.datetime.now()
print("用时：{},共捕捉图片：{}张,失败 ；{}".format(end-start,i - d,d))
# <dd title="收藏">111</dd>
#https://pixiv.bilibilinet.com/tags/%E4%B8%89%E7%8E%96/artworks?p=2&s_mode=s_tag
# 神楽七奈 アークナイツ1000users入り 五等分の花嫁1000users入り 俺ガイル1000users入り SAO1000users入 君の名は。1000users入 天気の子1000users入り アズールレーン1000users入り
# かぐや様は告らせたい 1000users入り





