## Welcome to xujinhao'python Pages

你可以访问我的 [bilibili](https://space.bilibili.com/666828747) 来关注我哦.

非常期待你的到来！

### faceswap

众所周知换脸是一件非常神奇的事情。

```markdown
import requests
import json
import simplejson
import base64
 
#第一步：获取人脸关键点
def find_face(imgpath):
    """
    :param imgpath: 图片的地址
    :return: 一个字典类型的人脸关键点 如：{'top': 156, 'left': 108, 'width': 184, 'height': 184}
    """
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect' #获取人脸信息的接口
    data = {
    "api_key":"",#访问url所需要的参数
    "api_secret":"",#访问url所需要的参数
    "image_url":imgpath, #图片地址
    "return_landmark":1
    }
    
    
    files = {'image_file':open(imgpath,'rb')} #定义一个字典存放图片的地址
    response = requests.post(http_url,data=data,files=files)
    res_con1 = response.content.decode('utf-8')
    res_json = simplejson.loads(res_con1)
    faces = res_json['faces']
    list = faces[0]
    rectangle = list['face_rectangle']
    return rectangle
 
#第二步：实现换脸
def merge_face(image_url1,image_url2,image_url,number):
    """
    :param image_url1: 被换脸的图片路径
    :param image_url2: 换脸的图片路径
    :param image_url: 换脸后生成图片所保存的路径
    :param number: 换脸的相似度
    """
    #首先获取两张图片的人脸关键点
    face1 = find_face(image_url1)
    face2 = find_face(image_url2)
    #将人脸转换为字符串的格式
    rectangle1 = str(str(face1['top']) + "," + str(face1['left']) + "," + str(face1['width']) + "," + str(face1['height']))
    rectangle2 = str(str(face2['top']) + "," + str(face2['left']) + "," + str(face2['width']) + "," + str(face2['height']))
    #读取两张图片
    f1 = open(image_url1,'rb')
    f1_64 = base64.b64encode(f1.read())
    f1.close()
    f2 = open(image_url2, 'rb')
    f2_64 = base64.b64encode(f2.read())
    f2.close()
    
    url_add = 'https://api-cn.faceplusplus.com/imagepp/v1/mergeface' #实现换脸的接口
    data={
    "api_key": "x2NyKaa6vYuArYwat4x0-NpIbM9CrwGU",
    "api_secret": "OuHx-Xaey1QrORwdG7QetGG5JhOIC8g7",
    "template_base64":f1_64,
    "template_rectangle":rectangle1,
    "merge_base64":f2_64,
    "merge_rectangle":rectangle2,
    "merge_rate":number
    }
    response1 = requests.post(url_add,data=data)
    res_con1 = response1.content.decode('utf-8')
    res_dict = json.JSONDecoder().decode(res_con1)
    result = res_dict['result']
    imgdata = base64.b64decode(result)
    file=open(image_url,'wb')
    file.write(imgdata)
    file.close()
 
if __name__ == '__main__':
    # face1=input('第一张图片（jpg）：')
    # face2=input('第二张图片（jpg）：')
    face1='1'
    face2='2'
    face3=face1+"_"+face2 #把face2的脸换到face1图片中的脸上去
    image1 = r""+face1+".jpg"
    image2 = r""+face2+".jpg"
    image3 = r""+face3+".jpg"
    merge_face(image1,image2,image3,100)

    
```
