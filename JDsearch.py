from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url='https://search.jd.com/Search?enc=utf-8&keyword='
word='手机'
page=1
resp=urlopen(url+request.quote(word)+'&page='+str(page))
bs=BeautifulSoup(resp.read(),'html.parser')

pageTag=bs.find('span',{"class":"fp-text"}).i
pageTotal=int(pageTag.text)

f=open('d:\\'+word+'.txt','wt')
for i in range(1,pageTotal):    
    page=i*2-1
    resp=urlopen(url+request.quote(word)+'&page='+str(page))
    bs=BeautifulSoup(resp.read(),'html.parser')

    productlist=bs.findAll('li',{"class":"gl-item"})
    for product in productlist:
        pid=product.get('data-pid')
        priceTag=product.find('div',{"class":"p-price"})
        iTag=priceTag.i
        if iTag:
            price=iTag.text
            nameTag=product.find('div',{"class":"p-name"})
            name=nameTag.em.text
        
            values=(pid,price,name)
            #print(values)
            f.write(str(values)+'\r\n')
    
f.close()
print('Done!')