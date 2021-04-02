#!/usr/bin/env python
# -*- coding:utf-8 -*-
#作者：どうでもいい菌
#网址：https://space.bilibili.com/450634867
import requests
import re
import os
import datetime
import urllib

ID = input('请输画师ID：')
URL_2 = input('请输画师url：')
while True:
    o_path = 'E:\编程\python\项目\爬取p站图片\【p站】画师特辑'
    # o_path = input('E:\编程\python\项目\爬取p站图片\【p站】画师特辑)：')
    if not os.path.exists(o_path):
        print('路径不存在!')
    else :
        break

start=datetime.datetime.now()
headers = {
    "cookie": "login_ever=yes; ki_r=; _ga=GA1.3.2013717293.1588508944; _ga=GA1.2.2013717293.1588508944; adr_id=HgGthok6pSrytKARGF4DEHpmUzCpDLr7G0mwm00p9gcnRt3N; _td=a4cb85b7-1b2f-4084-b5fa-8e96bc59d559; BNet=200624; _gid=GA1.2.297865900.1594310598; ki_t=1588508857697%3B1594434628989%3B1594474653479%3B15%3B31; yuid_b=lEWEEA; first_visit_datetime_pc=2020-07-11+22%3A37%3A45",  # 根据自己的浏览器情况填写，UA头也是
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "referer":"https://pixiv.bilibilinet.com/ajax/user/"+ID+"/profile/top?lang=zh"
}
URL_1 = "https://pixiv.bilibilinet.com/ajax/user/"+ID+"/profile/all?lang=zh"
# https://pixiv.bilibilinet.com/ajax/user/58338/profile/all?lang=zh
URL_2 = URL_2
# "https://pixiv.bilibilinet.com/ajax/user/"+ID+"/profile/illusts?ids%5B%5D=82847537&ids%5B%5D=82712750&ids%5B%5D=79898357&ids%5B%5D=78361191&ids%5B%5D=78171133&ids%5B%5D=78142008&ids%5B%5D=77377282&ids%5B%5D=76388370&ids%5B%5D=76010655&ids%5B%5D=75924201&ids%5B%5D=75878529&ids%5B%5D=75846578&ids%5B%5D=75827364&ids%5B%5D=74143874&ids%5B%5D=73805199&ids%5B%5D=73206388&ids%5B%5D=73011352&ids%5B%5D=72859871&ids%5B%5D=72329731&ids%5B%5D=72258923&ids%5B%5D=72175991&ids%5B%5D=72129699&ids%5B%5D=71902284&ids%5B%5D=71767940&ids%5B%5D=71492676&ids%5B%5D=71412590&ids%5B%5D=70095868&ids%5B%5D=69890358&ids%5B%5D=69782358&ids%5B%5D=69741328&ids%5B%5D=69154934&ids%5B%5D=69000947&ids%5B%5D=68986880&ids%5B%5D=68986842&ids%5B%5D=68542252&ids%5B%5D=66478995&ids%5B%5D=66360549&ids%5B%5D=66200809&ids%5B%5D=65998461&ids%5B%5D=65853035&ids%5B%5D=64323358&ids%5B%5D=64303890&ids%5B%5D=64268317&ids%5B%5D=63773649&ids%5B%5D=63140941&ids%5B%5D=62764772&ids%5B%5D=62227302&ids%5B%5D=62120962&work_category=illustManga&is_first_page=1&lang=zh"
JSON = requests.get(URL_1, headers=headers).json()

i = q = d = 0
file_path = o_path

print('共有作品：',len(JSON["body"]["illusts"]))
for result in JSON["body"]["illusts"]:

    id_1 = re.sub(': None', '', result)
    JSON = requests.get(URL_2, headers=headers).json()

    while i < len(JSON["body"]["works"]):
        try:
            url = JSON["body"]["works"][id_1]["url"]
            title = JSON["body"]["works"][id_1]["illustTitle"]
            userName = JSON["body"]["works"][id_1]["userName"]
            o_url_1 = re.sub('/c/250x250_80_a2', '', url)
            o_url = re.sub('square', 'master', o_url_1)

            information = "作品名称：" + title, "作品ID：" + str(id_1),  "作者姓名和ID：" + userName, str(ID)
            print(information)
            print(i + 1,'Downloading……')

            img_url = o_url
            file_name = "作品名称：" + title, "作品ID：" + str(id_1)

            try:
                if  os.path.exists(o_path + '\\' + userName):
                    pass
                else :
                    os.makedirs(o_path + '\\' + userName)
                    file_path = o_path + '\\' + userName

                file_suffix = os.path.splitext(img_url)[1]
                filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
                urllib.request.urlretrieve(img_url, filename=filename)

            except IOError as e:
                print("IOError")
                q += 1
            except Exception as e:
                print("Exception")
                q += 1
            d += 1
        except IOError as e:
            pass
        except Exception as e:
            pass
        i += 1
        break

end=datetime.datetime.now()
print("用时："+str(end-start),"成功："+str(d - q),"失败 ；" + str(q))

#
