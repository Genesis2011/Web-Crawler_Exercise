from urllib import request
import json

url1='http://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategory&callback=pcSeckillCategory'

resp = request.urlopen(url1)
data = resp.read().decode('utf-8')
data1 = data[ data.index('{') : -2]
jDecoder = json.JSONDecoder()
jObj = jDecoder.decode(data1)
categories = jObj.get('categories')

for category in categories:
    #print(category)
    cateId=category.get('cateId')
    sourceValue=category.get('sourceValue')
    #print(sourceValue)
    f=open('d:\\jdmiaosha'+sourceValue+'.csv','wt')
    
    #输出秒杀商品分类链接
    #url2='http://miaosha.jd.com/category.html?cate_id='+str(cateId)
    #print(url2)
    
    url2='http://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id='+str(cateId)
    respItem=request.urlopen(url2)
    dataItem = respItem.read().decode('utf-8')
    dataItem2 = dataItem[ dataItem.index('{')  :  -2]
    jDecoder = json.JSONDecoder()
    js2=jDecoder.decode(dataItem2)
    product0=js2.get('goodsList')[0]
    keys=list(product0.keys())
    keys.insert(0,'sourceValue')  
    
    f.write(str(keys))
    f.write('\r\n')    
    
    goodsLists=js2.get('goodsList')
    productAll=[]
    #print(goodsLists)
    
    for goodsList in goodsLists:
        #print(goodsList)
        valueList=list(goodsList.values())
        valueList.insert(0,sourceValue)
        values=str(valueList)
        #print(values)
        f.write(values[1:-1]+'\r\n')
        
    f.close()
    print(sourceValue+'.csv'+' Done!')
    
    

print('All Done!')