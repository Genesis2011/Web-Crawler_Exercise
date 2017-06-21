from urllib import request

url='https://miaosha.jd.com/'
html=request.urlopen(url)
data=html.read()

path='D:\\get_jdmiaosha.html'
f=open(path,'wb')
f.write(data)
f.close()