#-*-coding:utf-8-*-
import requests

url = ['https://api.douban.com/v2/book/']
status = {} 
list = ['title', 'origin_title','alt_title', 'subtitle','tags',  'author', 'author_intro', 'summary', 'rating', 'ebook_url',
          'translator', "pubdate", "publisher", 'price', 'binding', 'ebook_price','catalog','pages', "isbn10", "isbn13"]

def GetNmuber():
    _input = input('输入图书编码：')
    try:
        number = int(_input)
    except ValueError as e:
        print("请输入正确的只包含数字的图书编码。")
        return 
    url.append(_input)
    return GetUrl(url)

def GetUrl(url):
    web = ''.join(url)
    html = requests.get(web)
    if html.status_code == 404:
        print('未找到书目，请输入正确的图书编码')
        return
    SaveInfo(html)

def SaveInfo(html):
    hjson = html.json()
    for info in list:
        try:
            status[info]= hjson[info]
            OutputInfo(info)
        except:
            pass

def OutputInfo(info):
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