from urllib import request
import json

#商品列表，场次列表，品牌列表
url1='https://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&callback=pcMiaoShaAreaList&_=1498031871379'
#分类列表
url2='https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategory&callback=pcSeckillCategory&_=1498031871698'
#点击每一个分类，跳转的地址
url2_cate='https://miaosha.jd.com/category.html?cate_id=29'

#step1 获取json串
resp=request.urlopen(url1)
data=resp.read()
data1=data.decode('utf-8')

#step2 json串 掐头去尾
data2=data1[data1.index('{'):-2]

#step3 json解析
jDecoder=json.JSONDecoder()
js=jDecoder.decode(data2)

#得到miaoShaList
miaoShaList=js.get('miaoShaList')
#print(miaoShaList)
for product in miaoShaList:
    print(product)
