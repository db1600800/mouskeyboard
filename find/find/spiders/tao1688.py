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

def level1():
    url = 'https://www.1688.com/?spm=a2609.11712778.jizt5f4n.d5.8nq678'
    # 当前进程的工作目录
    cwd = getcwd()
    # 设置chrome驱动器
    driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    driver.set_page_load_timeout(2230)

    # 访问
    driver.get(url)
    print(url)


    # 获得网页内容
    summaryPage = driver.page_source
    driver.quit()
    # 解析HTML内容
    bs = BeautifulSoup(summaryPage, 'html.parser')
    # 通过Class获取内容
    summaryObjContent = bs.find_all(attrs={'class': 'left-box'})
    if summaryObjContent == None or summaryObjContent == "" or summaryObjContent == []:
        print(url + '  level1404' + '\n')
        driver.quit()

    level1 = []
    level1title=''
    for i in range(len(summaryObjContent)):

        lis = summaryObjContent[i].find_all('li')
        count=0
        for liitem in lis:
            if count<=5:
                count = count + 1
                continue
            ass = liitem.find_all('a')
            leibie = []
            for a in ass:
                url = a.get("href")
                txt = a.get_text()
                level1title=txt
                leibieitem = {'url': url, 'title': txt, 'level': '1'}
                level2result=level2(url)
                leibieitem["leve2"]=level2result
                leibie.append(leibieitem)
            level1.append(leibie)

            fo = open("1688" + level1title+".txt", "w+")  # 存入文件中。。。
            fo.write(json.dumps(level1))
            fo.write('\n')
            fo.close()
            count=count+1

    # 推出驱动并关闭所关联的所有窗口


    fo = open("1688"  + ".txt", "w+")  # 存入文件中。。。
    fo.write(json.dumps(level1))
    fo.write('\n')
    fo.close()



def level2(purl):
    url = purl
    # 当前进程的工作目录
    cwd = getcwd()
    # 设置chrome驱动器
    driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    driver.set_page_load_timeout(2230)

    # 访问
    driver.get(url)
    print(url)
    time.sleep(2)

    # 获得网页内容
    summaryPage = driver.page_source

    # 解析HTML内容
    bs = BeautifulSoup(summaryPage, 'html.parser')
    # 通过Class获取内容
    summaryObjContent = bs.find_all(attrs={'class': 'ch-menu-body'})
    if summaryObjContent == None or summaryObjContent == "" or summaryObjContent == []:
        print(url + '  level2404' + '\n')
        driver.quit()

    level2 = []

    for i in range(len(summaryObjContent)):

        lis = summaryObjContent[i].find_all('li')
        for liitem in lis:
            ass = liitem.find_all('a')
            leibie = []
            for a in ass:
                url = a.get("href")
                txt = a.get_text()
                leibieitem = {'url': url, 'title': txt, 'level': '2'}
                levellist=level2list(url)
                leibieitem["level2list"]=levellist
                leibie.append(leibieitem)
            level2.append(leibie)


    # 推出驱动并关闭所关联的所有窗口
    driver.quit()
    return  level2

def level2list(purl):
    url = purl
    # 当前进程的工作目录
    cwd = getcwd()
    # 设置chrome驱动器
    driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    driver.set_page_load_timeout(2230)

    # 访问
    driver.get(url)
    print(url)
    time.sleep(3)

    # 获得网页内容
    summaryPage = driver.page_source

    # 解析HTML内容
    bs = BeautifulSoup(summaryPage, 'html.parser')
    # 通过Class获取内容
    summaryObjContent = bs.find_all(attrs={'class': 'list'})
    if summaryObjContent == None or summaryObjContent == "" or summaryObjContent == []:
        print(url + '  level2list 404' + '\n')
        driver.quit()

    level2list = []
    for i in range(len(summaryObjContent)):

        lis = summaryObjContent[i].find_all(attrs={'class': 'cate1688-offer b2b-ocms-fusion-comp'})
        countitem=0
        for liitem in lis:
            ass = liitem.find_all('a')
            imgs = liitem.find_all('img')
            imgurl=''
            for imgu in imgs:
                index=imgu.get('src').find('310.')
                if (index != -1):
                    imgurl=imgu.get('src')

            leibie = []
            for a in ass:
                url = a.get("href")
                txt = a.get_text()

                moneystart=txt.find('￥')+1
                part2=txt.split('￥')[1]
                moneyend=part2.find('.')+moneystart+1

                money=txt[int(moneystart):int(moneyend)]

                print('listitem'+str(countitem)+' '+txt)
                leibieitem = {'url': url, 'title': txt,'imageurl':imgurl,'money':money,'level': '2list'}
                leibie.append(leibieitem)

            level2list.append(leibie)
            countitem=countitem+1

    driver.quit()
    # 推出驱动并关闭所关联的所有窗口
    return  level2list


if __name__ == '__main__':
    #getChapterUrl('http://ac.qq.com/Comic/ComicInfo/id/505435')
    #getChapterUrl('https://new.qq.com/omn/author/13030024')
    global gllmedia
    global n
    n=0
    global m
    m=0

    level1()





