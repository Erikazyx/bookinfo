#-*-coding:utf-8-*-
# import requests
# response = str(requests.get('https://api.douban.com/v2/book/1220562'))



from urllib.request import urlopen
import json
url = ['https://api.douban.com/v2/book/']
number = input('输入图书编码：')
url.append ( str(number))
web = ''.join(url)
html = urlopen(web)
# html = urlopen('https://api.douban.com/v2/book/1220562')

status = {'title':1, 'author':1, "pubdate":1, "publisher":1, 'summary':1, 'price':1, 'pages':1, "isbn10":1,"isbn13":1}
 
hjson = json.loads(html.read())
# dict={}
# a = hjson['rating'] ['average']#这里是得到花括号里面的子项
# print (a)


# 首先要得到书名'title'、评分'rating'(并打印出平均分)、作者名'author'然后按顺序打印出来

# 先考虑title和author 把他们存在dict当中
for info in status:
    status[info]= hjson[info]
    print(info,':\n',status[info])

# dict = {'a':1,'v':2}
# for i in dict :
#     print(i)