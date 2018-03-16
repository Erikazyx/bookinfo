#-*-coding:utf-8-*-
import requests

url = 'https://api.douban.com/v2/book/{}'
MAX_LEN = 140 
Sorts = ['title', 'origin_title','alt_title', 'subtitle','tags',  'author', 'author_intro', 'summary', 'rating', 'ebook_url',
          'translator', "pubdate", "publisher", 'price', 'binding', 'ebook_price','catalog','pages', "isbn10", "isbn13"]
D = {'title':'书名','origin_title':'原始书名','alt_title':'别名', 'subtitle':'副标题','tags':'标签',  'author':'作者', 'author_intro':'作者介绍', 'summary':'摘要', 'rating':'评分', 'ebook_url':'电子书地址',
     'translator':'翻译者', "pubdate":'出版日期', "publisher":'出版社', 'price':'价格', 'binding':'装订', 'ebook_price':'电子书价格','catalog':'目录','pages':'页数', "isbn10":'ISBN10', "isbn13":'ISBN13'}

def GetNmuber():
    _input = input('输入图书编码：')
    assert _input.isdigit() , '请输入正确的只包含数字的图书编码'
    return GetUrl(_input)

def GetUrl(_input):
    html = requests.get(url.format(_input))
    assert html.status_code == 200 ,'http error : code {}'.format(html.status_code)
    hjson = html.json()
    assert 'code' not in hjson,hjson.get('msg','api error,try again later')
    OutputInfo(hjson)

def OutputInfo(hjson):
    for i in Sorts:
        if i in hjson.keys():
            if len(hjson[i])==0:
                continue
            if i == 'tags':
                print('标签:')
                for n in hjson[i]:
                    print (n['name'],end=' ')
                print(' ')
                continue
            v = hjson[i][:MAX_LEN] + '...' if len(hjson[i]) > MAX_LEN else hjson[i]
            if i == 'rating':
                v = hjson['rating']['average']
            if isinstance(v, list):
                v = ','.join(hjson[i])
            i = D.get(i)
            print(i,':',v)

if __name__ == '__main__':
    GetNmuber()