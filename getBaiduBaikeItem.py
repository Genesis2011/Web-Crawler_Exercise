from urllib import request

def getBaike(word):
    word2=request.quote(word)
    url='http://baike.baidu.com/item/'+word2
    html=request.urlopen(url)
    data=html.read()

    path='d:\\baike_'+word+'.html'
    f=open(path,'wb')
    f.write(data)
    f.close()
    
    

getBaike('fedora')
getBaike('山东理工大学')