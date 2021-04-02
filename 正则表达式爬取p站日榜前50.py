# https://pixiv.bilibilinet.com/ranking.php

import requests
import re
import urllib
import os
import datetime
from datetime import date ,time,datetime,timedelta

p = input('是否直接爬取（y/n）:')

if p == 'y' :
    date = date.today()
    date = date.strftime('%Y%m%d')
    path = r'E:\python\项目\爬取p站图片\日榜\1-50'
else:
    date = input('请输入日期(20200713)：')
    path = input('请输入保存文件地址：')
url = "https://pixiv.bilibilinet.com/ranking.php?mode=daily&date="  + date
headers = {
    "cookie": "login_ever=yes; ki_r=; _ga=GA1.3.2013717293.1588508944; _ga=GA1.2.2013717293.1588508944; adr_id=HgGthok6pSrytKARGF4DEHpmUzCpDLr7G0mwm00p9gcnRt3N; _td=a4cb85b7-1b2f-4084-b5fa-8e96bc59d559; BNet=200624; ki_t=1588508857697%3B1593185098114%3B1593185098114%3B12%3B26; _gid=GA1.2.1544588426.1593614712; yuid_b=lmYHhTA; first_visit_datetime_pc=2020-07-02+00%3A04%3A38",  # 根据自己的浏览器情况填写，UA头也是
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "referer": "https://pixiv.bilibilinet.com/ranking.php?mode=daily&date="  + date
}

i = p = 0

Page = requests.get(url,headers=headers).text
urlList = re.findall(
    r'data-filter="thumbnail-filter lazy-image"data-src="(.+?.jpg)"',Page)

for url in urlList:
    o_url = re.sub('c/240x480/','',url)
    print(o_url)
    i +=1

    img_url = o_url
    file_path = path
    file_name = i

    try:

        if not os.path.exists(file_path):

            os.makedirs(file_path)
        file_suffix = os.path.splitext(img_url)[1]
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        urllib.request.urlretrieve(img_url, filename=filename)

    except IOError as e:
        print("IOError")
        p += 1
    except Exception as e:
        print("Exception")
print('爬取数量：'+str(i))







