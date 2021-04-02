#!/usr/bin/env python
# -*- coding:utf-8 -*-
#作者：どうでもいい菌
#网址：https://space.bilibili.com/450634867
import requests
import os
import time
import urllib
import re
import datetime
from datetime import date
import requests
from PIL import Image
from io import BytesIO

start = datetime.datetime.now()
input_file = 'E:\编程\python\项目\爬取p站图片\【p站】画师特辑\information.txt'
filereader = open(input_file, 'r',encoding='utf_8')
allid = filereader.readlines(0)

for id1 in allid:
    ID =  re.sub('\n', '', id1)
    while True:
        o_path = 'E:\编程\python\项目\爬取p站图片\【p站】画师特辑'
        # o_path = input('E:\编程\python\项目\爬取p站图片\【p站】画师特辑)：')
        if not os.path.exists(o_path):
            print('路径不存在!')
        else :
            break

    headers = {
        'authority': 'www.pixiv.net',
        'cache-control': 'no-cache',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^88^\\^, ^\\^Google',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pixiv.net/users/83739',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'cookie': 'first_visit_datetime_pc=2020-08-16+23^%^3A41^%^3A10; p_ab_id=9; p_ab_id_2=7; p_ab_d_id=1276670180; yuid_b=JmmGJiE; __utmz=235335808.1597588883.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none); _ga=GA1.2.1238364322.1597588883; c_type=16; a_type=0; b_type=1; ki_r=; login_ever=yes; __utmv=235335808.^|2=login^%^20ever=yes=1^^3=plan=normal=1^^5=gender=male=1^^6=user_id=52639055=1^^9=p_ab_id=9=1^^10=p_ab_id_2=7=1^^11=lang=zh=1; __utma=235335808.1238364322.1597588883.1598515773.1598713274.3; ki_s=209879^%^3A0.0.0.0.0; PHPSESSID=52639055_oEEsIDRIP3admKE1Zp1Ej6JlIFyHzjFr; privacy_policy_agreement=2; __cfduid=da0fc77c4570636e5fc35eae2c1a811f21612649420; tag_view_ranking=RTJMXD26Ak~jH0uD88V6F~Ie2c51_4Sp~kP7msdIeEU~bjwhesOPOI~3mLXnunyNA~v3nOtgG77A~VbPCYJXdEP~E-VllraUle~ZNjyiEyrTB~1bPq20eRbM~fg8EOt4owo~uusOs0ipBx~RcahSSzeRf~Dd2BFtvC_a~X_1kwTzaXt~w8ffkPoJ_S~Lt-oEicbBr~S3uWLakKP-~CrFcrMFJzz~_4AOSbC75r~XJzl0dPLDN~xBU5v8UUGM~Wzi7sMlG7S~D0nMcn6oGk~-StjcwdYwv~QaiOjmwQnI~jk9IzfjZ6n~qcYo_5oqVP~q303ip6Ui5~qa8ep1CwpY~BU9SQkS-zU~y8GNntYHsi~xq14noDNQh~cB7561aCil~NpsIVvS-GF~_hSAdpN9rx~Abey9BvU2h~i-US0_DQLY~qtytUjlJg7~jhuUT0OJva~e4ea3ikQSl~9ODMAZ0ebV~fR8eZGJTfM~OEHogw1GmU~zIv0cf5VVk~-IrOV3901X~BEa426Zwwo~ZZltVrbyeV~WY10GFG4q3~a-IhwNF_3B~R8gaK-u6bh~isFf_CMYqz~nQRrj5c6w_~ahHegnNVxX~cuLB4S02iF~CBKuoUuA6J~MhieHQxNXo~aWKnJBSaY2~4rDNkkAuj_~ln7cvgryTu~gatroTOnfX~VN4GiXVEHh~OT4SuGenFI~BYbAF8suC-~RKAHEY3QDd~QwQ3wReUTs~5KvHjAz-dp~ZXFMxANDG_~s-c3WFDdik; __cf_bm=2d0be96bf3decceeb95d88e421532b6b6d96d87b-1612655212-1800-AXIsMEF4pYzobnD4SBuqMp78rikF6qWATFqrmN7P67b/pebAfjfsJ0CkhjaPiADAEZ0vDuwYMjS3bFHJGk+CKnU=; ki_t=1597588951284^%^3B1612649422265^%^3B1612655215875^%^3B6^%^3B16',
        'Referer': 'https://www.pixiv.net/users/83739',
        'Origin': 'https://www.pixiv.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'if-modified-since': 'Wed, 27 Jan 2021 09:17:19 GMT',
        'x-user-id': '52639055',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'If-None-Match': 'W/^\\^c8193eb44fb89c3c1f18d9d42944419d^\\^',
        'If-Modified-Since': 'Sun, 10 Jan 2021 15:00:56 GMT',
        'origin': 'https://www.pixiv.net',
        'if-none-match': 'W/^\\^dc38bc0c8df731af48f9c4b79c16bff9^\\^',
        'Upgrade-Insecure-Requests': '1',
        'pragma': 'no-cache',
    }
    URL_1 = "https://www.pixiv.net/ajax/user/"+ID+"/profile/all?lang=zh"
    URL_2 = "https://www.pixiv.net/ajax/user/"+ID+"/profile/top?lang=zh"
    JSON = requests.get(URL_1, headers=headers).json()

    i = q = 0
    file_path = o_path

    for result in JSON["body"]["illusts"]:

        id_1 = re.sub(': None', '', result)
        JSON = requests.get(URL_2, headers=headers).json()
        if i==24 :
            break
        while i < len(JSON["body"]["illusts"]):

            url = JSON["body"]["illusts"][id_1]["url"]
            title = JSON["body"]["illusts"][id_1]["title"]
            userName = JSON["body"]["illusts"][id_1]["userName"]
            o_url_1 = re.sub('/c/250x250_80_a2/img-master', '/img-original', url)
            o_url = re.sub('_square1200.jpg', '.png', o_url_1)

            information = "作品名称：" + title, "作品ID：" + str(id_1),  "作者姓名和ID：" + userName, str(ID)
            print(information)
            print(i + 1,o_url,'Downloading……')
            '''
            https://i.pximg.net/c/250x250_80_a2/img-master/img/2019/12/23/21/49/00/78442710_p0_square1200.jpg
             https://i.pximg.net/img-master/img/2021/02/05/00/00/05/87535238_p0_master1200.jpg
             https://i.pximg.net/img-original/img/2021/02/05/00/00/05/87535238_p0.png
            '''
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
                # urllib.request.urlretrieve(img_url, filename=filename)
                img_src = o_url
                response = requests.get(img_src, headers=headers)
                image = Image.open(BytesIO(response.content))
                image.save(filename)



            except IOError as e:
                print("IOError")
                q += 1
            except Exception as e:
                print("Exception")
                q += 1
            i += 1
            break

end=datetime.datetime.now()
print("用时："+str(end-start),"成功："+str(i - q),"失败 ；" + str(q))

