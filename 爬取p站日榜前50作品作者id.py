#!/usr/bin/env python
# -*- coding:utf-8 -*-
#作者：どうでもいい菌
#网址：https://space.bilibili.com/450634867
import requests
import os
import urllib
import re
import datetime
from datetime import date

i = j = q = 0
# s = input('是否直接爬取1-50（y/n）:')


yesterday = str(int(date.today().strftime('%Y%m%d'))-2)
# os.makedirs('E:\编程\python\项目\爬取p站图片\日榜\\1-50\\'+yesterday)
path = 'E:\编程\python\项目\爬取p站图片\【p站】画师特辑'
date_1 = yesterday
p = 1#页数

start=datetime.datetime.now()
headers = {
    "cookie": "first_visit_datetime_pc=2020-08-16+23%3A41%3A10; p_ab_id=9; p_ab_id_2=7; p_ab_d_id=1276670180; yuid_b=JmmGJiE; __utmz=235335808.1597588883.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1238364322.1597588883; c_type=16; a_type=0; b_type=1; ki_r=; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=52639055=1^9=p_ab_id=9=1^10=p_ab_id_2=7=1^11=lang=zh=1; __utma=235335808.1238364322.1597588883.1598515773.1598713274.3; ki_s=209879%3A0.0.0.0.0; PHPSESSID=52639055_oEEsIDRIP3admKE1Zp1Ej6JlIFyHzjFr; privacy_policy_agreement=2; __cfduid=da0fc77c4570636e5fc35eae2c1a811f21612649420; tag_view_ranking=RTJMXD26Ak~jH0uD88V6F~Ie2c51_4Sp~kP7msdIeEU~bjwhesOPOI~3mLXnunyNA~v3nOtgG77A~VbPCYJXdEP~E-VllraUle~ZNjyiEyrTB~1bPq20eRbM~fg8EOt4owo~uusOs0ipBx~RcahSSzeRf~Dd2BFtvC_a~X_1kwTzaXt~w8ffkPoJ_S~Lt-oEicbBr~S3uWLakKP-~CrFcrMFJzz~_4AOSbC75r~XJzl0dPLDN~xBU5v8UUGM~Wzi7sMlG7S~D0nMcn6oGk~-StjcwdYwv~QaiOjmwQnI~jk9IzfjZ6n~qcYo_5oqVP~q303ip6Ui5~qa8ep1CwpY~BU9SQkS-zU~y8GNntYHsi~xq14noDNQh~cB7561aCil~NpsIVvS-GF~_hSAdpN9rx~Abey9BvU2h~i-US0_DQLY~qtytUjlJg7~jhuUT0OJva~e4ea3ikQSl~9ODMAZ0ebV~fR8eZGJTfM~OEHogw1GmU~zIv0cf5VVk~-IrOV3901X~BEa426Zwwo~ZZltVrbyeV~WY10GFG4q3~a-IhwNF_3B~R8gaK-u6bh~isFf_CMYqz~nQRrj5c6w_~ahHegnNVxX~cuLB4S02iF~CBKuoUuA6J~MhieHQxNXo~aWKnJBSaY2~4rDNkkAuj_~ln7cvgryTu~gatroTOnfX~VN4GiXVEHh~OT4SuGenFI~BYbAF8suC-~RKAHEY3QDd~QwQ3wReUTs~5KvHjAz-dp~ZXFMxANDG_~s-c3WFDdik; ki_t=1597588951284%3B1612649422265%3B1612650253137%3B6%3B14; __cf_bm=bcc05d4cde2150d4b952c75126d75574e3f3672b-1612651103-1800-ASAzXAM9w8it599M1YF4nDJjU423f3iTt5OQTj+U+7X/Motg1YZlKwHhOVONBEAYAVenwiFrDMQx39Msckgt2+Y=",  # 根据自己的浏览器情况填写，UA头也是
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
    "referer": "https://www.pixiv.net/ranking.php?mode=daily&date="+date_1+"&p="+str(p)+"&format=json"
}
'''
https://www.pixiv.net/ranking.php?p=2&format=json
https://www.pixiv.net/ranking.php?mode=daily&date=20210205&p=2&format=json"
'''
URL = "https://www.pixiv.net/ranking.php?mode=daily&date="+date_1+"&p="+str(p)+"&format=json"
session = requests.get(URL, headers=headers)
JSON = session.json()

while i < len(JSON["contents"]):

    user_id = JSON["contents"][i]["user_id"]
    information = str(user_id)
    i += 1

    print(information)

    if i<=12 :
        with open(path + '\information.txt','ab') as file_handle:  # .txt可以不自己新建,代码会自动新建
            file_handle.write(information.encode('utf-8'))
            file_handle.write('\n'.encode('utf-8'))  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
    if 12<i<=24:
        with open(path + '\information2.txt', 'ab') as file_handle:  # .txt可以不自己新建,代码会自动新建
            file_handle.write(information.encode('utf-8'))
            file_handle.write('\n'.encode('utf-8'))
    if 24 < i <= 36:
        with open(path + '\information3.txt', 'ab') as file_handle:  # .txt可以不自己新建,代码会自动新建
            file_handle.write(information.encode('utf-8'))
            file_handle.write('\n'.encode('utf-8'))
    if 36 < i <= 50:
        with open(path + '\information4.txt', 'ab') as file_handle:  # .txt可以不自己新建,代码会自动新建
            file_handle.write(information.encode('utf-8'))
            file_handle.write('\n'.encode('utf-8'))

end=datetime.datetime.now()
print("用时："+str(end-start))


