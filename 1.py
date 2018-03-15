#-*-coding:utf-8-*-

from urllib.request import urlopen
import json

url = ['https://api.douban.com/v2/book/']
status = {'title':1, 'author':1, 'summary':1, 'rating':1, 'tags':1, "pubdate":1, "publisher":1, 'price':1, 'pages':1, "isbn10":1, "isbn13":1} 

def GetNmuber():
    inpu = input('输入图书编码：')
    try:
        number = None
        number = int(inpu)
    except ValueError as e:
        print("请输入正确的只包含数字的图书编码。")
        return 
    url.append(inpu)
    return GetUrl(url)

def GetUrl(url):
    web = ''.join(url)
    try:
        html = urlopen(web)
    except:
        print('未找到书目，请输入正确的图书编码')
        return
    return OutPutInfo(html)
    

def OutPutInfo(html):
    hjson = json.loads(html.read().decode('utf-8'))
    for info in status:
        status[info]= hjson[info]
        if info == 'summary':
            print(info,':\n',status[info])
        elif info == 'author':
            if len(status[info])!=0:
                print(info,':',status[info][0])
            else:
                print(info,':','未找到')
        elif info == 'tags':
            print("tags:")
            for i in status[info]:
                print (i['name'],end=" ")
            print(' ')
        elif info =='rating':
            print('rating:',hjson['rating'] ['average'])
        else:
            print(info,':',status[info])

GetNmuber()