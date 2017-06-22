from bs4 import BeautifulSoup
from urllib.request import urlopen

resp=urlopen('http://www.jd.com')
bs=BeautifulSoup(resp.read(),'html.parser')
head=bs.head
body=bs.body
div=bs.find('div',{"class":"J_cate cate"})

catelist=bs.findAll('li',{"class":"cate_menu_item"})
for cate in catelist:
    print(cate.text.replace('\n',''))