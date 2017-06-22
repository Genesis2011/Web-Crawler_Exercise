from urllib import request
import json

#url1='http://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&callback=pcMiaoShaAreaList&_=1498031884735'
url1='http://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategory&callback=pcSeckillCategory&_=1498099636710'

resp = request.urlopen(url1)
data = resp.read().decode('utf-8')
data1 = data[ data.index('{') : -2]
jDecoder = json.JSONDecoder()
jObj = jDecoder.decode(data1)
categories = jObj.get('categories')

for category in categories:
    #print(category)
    cateId=category.get('cateId')
    #print(cateId)
    
    url2='http://miaosha.jd.com/category.html?cate_id='+str(cateId)
    print(url2)
    #输出秒杀商品分类链接