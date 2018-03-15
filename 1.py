#-*-coding:utf-8-*-

from urllib.request import urlopen
import json

url = ['https://api.douban.com/v2/book/']
status = {} 
list = ['title', 'origin_title','alt_title', 'subtitle','tags',  'author', 'author_intro', 'summary', 'rating', 'ebook_url',
          'translator', "pubdate", "publisher", 'price', 'binding', 'ebook_price','catalog','pages', "isbn10", "isbn13"]
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
    return SaveInfo(html)
    

def SaveInfo(html):
    hjson = json.loads(html.read().decode('utf-8'))
    for info in list:
        try:
            status[info]= hjson[info]
        except:
            pass
    return OutputInfo()

def OutputInfo():
    for info in list:
        if not status.get(info):
            pass
        elif info == 'summary' or info =='author_intro':
            print(info,':\n',status[info])
        elif info == 'rating':
            print(info,':',status[info]['average'])
        elif info =='author' or info == 'translator':
            for i in status[info]:
                print(info,':',i)
        elif info =='tags':
            print('tags:')
            for i in status[info]:
                print (i['name'],end=' ')
            print(' ')
        else:
            print(info,':',status[info])


GetNmuber()