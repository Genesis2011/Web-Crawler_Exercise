from urllib import request
from bs4 import BeautifulSoup

#jd搜索的URL地址，需要带keyword和page参数
url='https://search.jd.com/Search?enc=utf-8&keyword='

#定义搜索关键词
word='手机'
#当前页数
page=1
#总页数
pageTotal=1

resp = request.urlopen(url+request.quote(word) +'&page='+str(page))
bs = BeautifulSoup(resp.read(), 'html.parser')

#解析总页数
pageTag = bs.find('span',{"class":"fp-text"}).i
pageTotal = int(pageTag.text)

#得到商品的li节点列表 
productlist = bs.findAll('li',{"class":"gl-item"})
for product in productlist:
    #print(product)
    #product：具体商品的 li节点
    
    #得到商品的pid
    pid = product.get('data-pid')
    price = ''
    
    #得到商品的 价格 节点
    priceTag=product.find('div',{"class":"p-price"})
    iTag = priceTag.i
    if iTag:price = iTag.text
    
    #得到商品的 名称 节点
    nameTag=product.find('div',{"class":"p-name"})
    name=nameTag.em.text
    
    #打印结果
    value=(pid,price,name)
    print(value)
