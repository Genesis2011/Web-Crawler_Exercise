from urllib import request
import json

#商品列表，场次列表，品牌列表
url1='http://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&callback=pcMiaoShaAreaList&_=1498031884735'

resp = request.urlopen(url1)
data = resp.read().decode('utf-8')

data1 = data[ data.index('{') : -2]

jDecoder = json.JSONDecoder()
jObj = jDecoder.decode(data1)

product0=jObj.get('miaoShaList')[0]
keys=list(product0.keys())
keys.insert(0,'startTime')

#场次对象
groups = jObj.get('groups')

#所有场次的商品列表 
productAll=[]
f=open('d:\\jdmiaosha.csv','wt')
f.write(str(keys[1:-1]))
f.write('\r\n')

for group in groups:
    gid=group.get('gid')
    startTime=group.get('startTime')
    
    #每个场次的列表
    url2=url1+'&gid='+str(gid)
    #print(url2)
    respItem=request.urlopen(url2)
    
    dataItem = respItem.read().decode('utf-8')
    dataItem2 = dataItem[ dataItem.index('{')  :  -2]
    jDecoder = json.JSONDecoder()
    js2=jDecoder.decode(dataItem2)
    #print(js2)
    
    #每个场次的商品列表
    products = js2.get('miaoShaList')
    for product in products:
        #取每个商品json对象的值列表，并进行字符串的转换
        #print(product)
        valueList=list(product.values())
        valueList.insert(0,startTime)
        values=str(valueList)
        #print(values)
        #写文件
        f.write(values[1:-1]+'\r\n')
        
    
f.close()
print('Done!')