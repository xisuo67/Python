#-*- coding:utf-8 -*-
import re,requests,os
#url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1460997499750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%B0%8F%E9%BB%84%E4%BA%BA'
word = raw_input("请输入要下载的图片关键字: ")
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
html = requests.get(url).text

#html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
i = 0
for each in pic_url:
    print each
    try:
        pic= requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print '【错误】当前图片无法下载'
        continue
    string = 'pictures\\'+str(i) + '.jpg'
    if(os.path.exists('./pictures')!=True):  #判断文件夹是否存在，不存在则创建文件夹
        os.mkdir('./pictures')
    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()
    i += 1



