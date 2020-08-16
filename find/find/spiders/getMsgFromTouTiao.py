import json
import random
import os
import re
from selenium import webdriver
from os import getcwd,sep
from bs4 import BeautifulSoup

from qqkeyboard_getmsg import *
from qqkeyboard_getmsg import MouseActionExecute_part_selectcity


def getMsgFromToutiao(startExecuteBtn):
    global execWhichStep
    area1_xiaoqufile = open("area_page3.json", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    partOneObjs = json.loads(filecontent)
    citys = partOneObjs.keys()
    # citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']
    #citys = ['佛山']
    searchStr = ""
    requestAddStr = ""
    xiaoquDateAddCount = 30
    count = 0
    countquery = 0
    qqfobiden = 0
    for city in citys:
        countys = partOneObjs[city].keys()
        for county in countys:

            #chose = whichCity(city, startExecuteBtn)
            #if chose == False:
             #   continue

            areas = partOneObjs[city][county].keys()
            print(city+" "+county+" ")

            execWhichStep = "toutiao选城市取数据/1今日头条1定位到地方.txt"
            startExecuteBtn['text'] = execWhichStep
            t3 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t3.start()
            t3.join()
            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/1今日头条1定位到地方.txt"
            startExecuteBtn['text'] = execWhichStep
            t3 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t3.start()
            t3.join()
            time.sleep(10)

            execWhichStep = "toutiao选城市取数据/2进入选地方.txt"
            startExecuteBtn['text'] = execWhichStep
            # UIUpdateCutDownExecute(6, custom_thread_list).start()
            t21 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t21.start()
            t21.join()
            time.sleep(3)



            execWhichStep = "toutiao选城市取数据/2.1城市/2.1"+city+".txt"
            startExecuteBtn['text'] = execWhichStep
            t21 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t21.start()
            t21.join()

            time.sleep(3)

            execWhichStep = "toutiao选城市取数据/3.1选择进入抓包软件HttpCanary3.txt"
            startExecuteBtn['text'] = execWhichStep
            t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t31.start()
            t31.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/3.2选择第一项抓包列表.txt"
            startExecuteBtn['text'] = execWhichStep
            t32 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t32.start()
            t32.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/3.3进入请求结果.txt"
            startExecuteBtn['text'] = execWhichStep
            t33 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t33.start()
            t33.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/3.4点请求结果详情.txt"
            startExecuteBtn['text'] = execWhichStep
            t34 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t34.start()
            t34.join()

            time.sleep(6)
            execWhichStep = "toutiao选城市取数据/3.5保存结果.txt"
            startExecuteBtn['text'] = execWhichStep
            t35 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t35.start()
            t35.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/3.6返回抓包主页.txt"
            startExecuteBtn['text'] = execWhichStep
            t36 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t36.start()
            t36.join()

            time.sleep(4)
            execWhichStep = "toutiao选城市取数据/4.1选择进入文件管理软件4-已初始can-json-选好第一项.txt"
            startExecuteBtn['text'] = execWhichStep
            t41 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t41.start()
            t41.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/4.2点json文件夹.txt"
            startExecuteBtn['text'] = execWhichStep
            t42 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t42.start()
            t42.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/4.2.1点json文件夹.txt"
            startExecuteBtn['text'] = execWhichStep
            t42 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t42.start()
            t42.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/4.3不用勾选删除第一项.txt"
            startExecuteBtn['text'] = execWhichStep
            t43 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t43.start()
            t43.join()

            time.sleep(3)
            execWhichStep = "toutiao选城市取数据/4.4勾选第一项发送dbbqbq.txt"
            startExecuteBtn['text'] = execWhichStep
            t44 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t44.start()
            t44.join()

            time.sleep(6)
            execWhichStep = "toutiao选城市取数据/4.4.1在qq2上选dbbqbq.txt"
            startExecuteBtn['text'] = execWhichStep
            t44 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t44.start()
            t44.join()

            time.sleep(3)
            execWhichStep = "toutiao选城市取数据/4.5qq2软件上点发送文件按钮.txt"
            startExecuteBtn['text'] = execWhichStep
            t45 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t45.start()
            t45.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/5回到今日头条.txt"
            startExecuteBtn['text'] = execWhichStep
            t5 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t5.start()
            t5.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/6.1qq接收文件.txt"
            startExecuteBtn['text'] = execWhichStep
            t61 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t61.start()
            t61.join()

            time.sleep(2)
            execWhichStep = "toutiao选城市取数据/6.2打开文件.txt"
            startExecuteBtn['text'] = execWhichStep
            t62 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t62.start()
            t62.join()

            time.sleep(5)
            execWhichStep = "toutiao选城市取数据/6.3全选内容并复制.txt"
            startExecuteBtn['text'] = execWhichStep
            t63 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t63.start()
            t63.join()

            msgStr = getClipboardText()
            citynewslist(msgStr,city)
            print(msgStr)
            print("getmsg 完成")


            for area in areas:
                xiaoqus = partOneObjs[city][county][area].keys()
                for xiaoqu in xiaoqus:

                    xiaoqudict = partOneObjs[city][county][area][xiaoqu]
                    if xiaoqudict.get("isRequestQQGroup") == True:
                        xiaoquname = xiaoqudict["xiaoquname"]
                        href = xiaoqudict["href"]
                        address = xiaoqudict["address"]
                        dong = xiaoqudict["dong"]
                        fengqi = xiaoqudict["fengqi"]

                        #time.sleep(120)


    area1_xiaoqufile.close()


def whichCity(city,startExecuteBtn):
    chose=False
    if city == "中山":
        chose = True
    """
    if city == "珠海":
        chose = True
    
    if city == "郑州":
        chose = True
    """
    return chose


def citynewslist(newsstr,city):
    citynewsObjs = json.loads(newsstr)
    if citynewsObjs==None:
        return
    strcity=citynewsObjs["location"]["city_name"]
    total_number=citynewsObjs["total_number"]
    if strcity==city:
        datas=citynewsObjs["data"]
        for contentStr in datas:
           contentobj= json.loads(contentStr["content"])
           article_url=contentobj["article_url"]
           if article_url!="":
            nearby_read_info=contentobj["nearby_read_info"]
            title=contentobj["title"]
            abstract=contentobj["abstract"]
            divhtml=parse_article(article_url)
            htmlcreate(title,divhtml)


def parse_article(aurl):
    url =aurl
    # 当前进程的工作目录
    cwd = getcwd()
    # 设置chrome驱动器
    driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    driver.set_page_load_timeout(223)

    # 访问
    driver.get(url)
    print(url)
    time.sleep(5)
    # 获得网页内容
    summaryPage = driver.page_source
    # 解析HTML内容
    summaryObj = BeautifulSoup(summaryPage, 'html.parser',from_encoding="utf-8")
    prety = summaryObj.prettify()
    # print prety
    pointed_div = summaryObj.findAll(name="div",
                               attrs={"class": re.compile("article-box")})
    if pointed_div==[]:
     pointed_div = summaryObj.findAll(name="video")
    #driver.quit()
    # 筛选标签为div且属性class为forFlow的源码
    return  pointed_div


def htmlcreate(title,divhtml):
    str+='<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "//www.wapforum.org/DTD/xhtml-mobile10.dtd" > \n'
    str+='<html xmlns="http://www.w3.org/1999/xhtml" lang="zh-CN" >\n'
    str+='<head>\n'
    str+='<meta name="applicable-device" content="mobile" >\n'
    str+='<meta http-equiv="Content-Type" content="text/html; charset=utf-8" / >\n'
    str+='<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" / >\n'
    str+='<meta name="format-detection" content="telephone=no" / >\n'
    str+='<meta name="apple-mobile-web-app-capable" content="yes" / >\n'
    str+='<title> '+title+' </title>\n'

    str+='<link href="mnewcss.css" rel="stylesheet" type="text/css" / >\n'
    str+='<link href="toutiao.css" rel="stylesheet" type="text/css" / >\n'
    str+='</head>\n'
    str+='<body>\n'
    str+='<div class="ssi_headB_jxwd_m" ></div>\n'

    str+='<div class="main" >\n'

    str+='<div id="new-style" class="bui-box article-content-container" >\n'

    str+='<div class="bui-left index-middle" >\n'

    str+=divhtml+'\n'

    str+='</div>\n'
    str+='</div>\n'

    str+='<div class="unfold-field" id="unfold-field" onclick="javascript:showAll()" >\n'

    str+='<div class="unflod-field__mask"> </div>\n'

    str+='<a href="javascript:showAll()" class="unfold-field__text" > 展开全文 </a>\n'

    str+='</div>\n'
    str+='</div>\n'

    str+='<script>\n'
    str+='function showAll()\n'
    str+='{\n'
    str+='var obj=document.getElementById(\'new-style\');\n'
    str+='var obja=document.getElementById(\'unfold-field\');\n'
    str+='obja.style.display="none";\n'
    str+='obj.style.height="inherit";\n'
    str+='}\n'
    str+='</script>\n'

    str+='<div class="instop-r">\n'

    str+='<div class="icautojz">\n'

    str+='<div class="hiddenjz">\n'

    str+='<ul>\n'
    str+='<li>\n< a href="https://m.icauto.com.cn/zdm/66/664887.html">\n'
    str+='<div class="instop-img" >\n'
    str+='<img src="https://imgs.icauto.com.cn/allimg/randImg/allrand/3675.jpg" realSrc="https://imgs.icauto.com.cn/allimg/randImg/allrand/3675.jpg" / >\n'
    str+='</div>\n'
    str+='<div class="instop-t-new" > 减震器坏了有什么症状，汽车减震器坏了的表现 </div>\n'
    str+='< div class="instop-t-time" > 2019-12-19 < / div >\n'
    str+='</a>\n'
    str+='</li>\n'
    str+='</ul>\n'
    str+='</div>\n'
    str+='</div>\n'
    str+='</div>\n'
    str+='</body>\n'
    str+='</html>\n'
