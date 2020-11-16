import os
import time
import requests
from selenium import webdriver
from os import getcwd,sep
from bs4 import BeautifulSoup
import json


global allmedia
allmedia={}
global n
global m

def inivalue():
    global allmedia
    global n
    media8 = open("tenxunmedia_" + str(n) + ".txt", 'r+', encoding='utf-8')
    filecontent = media8.read()
    allmedia = json.loads(filecontent)

if __name__ == '__main__':
    #getChapterUrl('http://ac.qq.com/Comic/ComicInfo/id/505435')
    #getChapterUrl('https://new.qq.com/omn/author/13030024')
    global gllmedia
    global n
    n=0
    global m
    m=0

    inivalue()

    ii=13004463 #13030024 13001294
    while True:
        url='https://new.qq.com/omn/author/'+str(ii)
        # 当前进程的工作目录
        cwd = getcwd()
        # 设置chrome驱动器
        driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
        # 设置超时时间
        driver.set_page_load_timeout(223)

        # 访问
        driver.get(url)
        print(url)

        ii += 1
        # 获得网页内容
        summaryPage = driver.page_source
        # 解析HTML内容
        summaryObj = BeautifulSoup(summaryPage, 'html.parser')
        # 通过Class获取内容
        summaryObjContent = summaryObj.find_all(attrs={'class': 'author-name'})
        if summaryObjContent==None or summaryObjContent=="" or summaryObjContent==[]:
            print(url + '  404' + '\n')
            driver.quit()
            continue

        for i in range(len(summaryObjContent)):
            # 查找出一个a标签
            #aObj = summaryObjContent[i].find('a')
            # 查a标签的href值
            #href = aObj['href']
            # 标签<a>中含有其他标签，用k.get_text()
            # strip()方法，去除字符串开头或者结尾的空格
            #title = aObj.get_text().strip()

            title=summaryObjContent[i].text
            obj = {}
            obj["title"] = title
            obj["url"] = url
            allmedia[title] = obj

            print(title + ' url '+url+ '\n')

        if m!=0 and m%50==0:
            fo = open("tenxunmedia_" + str(n) + ".txt", "w+")  # 存入文件中。。。
            fo.write(json.dumps(allmedia))
            fo.write('\n')
            fo.close()
            print( ' 50 write file '  + '\n')

        if m % 2000 == 0:
            n += m // 2000
            print(' 2000  n :' +str(n)+'\n')

        if m % 2000 == 0:
            if m != 0:
                allmedia = {}
        m+=1
        # 推出驱动并关闭所关联的所有窗口
        driver.quit()
