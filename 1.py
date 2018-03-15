#-*-coding:utf-8-*-

from urllib.request import urlopen
import json

url = ['https://api.douban.com/v2/book/']
status = {'title':1, 'origin_title':1,'alt_title':1, 'subtitle': '','tags':1,  'author':1, 'author_intro':1, 'summary':1, 'rating':1, 'ebook_url':1,
          'translator':1, "pubdate":1, "publisher":1, 'price':1, 'binding':1, 'ebook_price':1,'catalog':1,'pages':1, "isbn10":1, "isbn13":1} 

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
        try:
            status[info]= hjson[info]
            if len(status[info])==0:
                pass
            elif info == 'summary' or info =='author_intro':
                print(info,':\n',status[info])
            elif info == 'author' or info =='translator':
                print(info,':',status[info][0])
            elif info == 'tags':
                print("tags:")
                for i in status[info]:
                    print (i['name'],end=" ")
                print(' ')
            elif info =='rating':
                print('rating:',hjson['rating'] ['average'])
            else:
                print(info,':',status[info])
        except:
            pass


GetNmuber()