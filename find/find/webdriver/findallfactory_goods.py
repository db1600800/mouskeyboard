import json
import random
import os
import re
from selenium import webdriver
from os import getcwd,sep
from bs4 import BeautifulSoup
import json
import time
import urllib.request
from qqkeyboard_addgroup import *






def goods():
    area1_xiaoqufile = open("1688产品/智能锁工厂_产品.txt", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    companys = json.loads(filecontent)
    area1_xiaoqufile.close()

    cwd = getcwd()
    # 设置chrome驱动器
    driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    driver.set_page_load_timeout(2230)

    # cookies = driver.get_cookies()

    driver.delete_all_cookies()

    js = 'window.open("https://www.baidu.com");'  # 通过执行js，开启一个新的窗口
    driver.execute_script(js)



    countcompany=0
    countcompanylogin=0
    for company in companys:
            if countcompany<332:
                countcompany+=1
                continue
            countcompany+=1

            if countcompany%10==0:
                time.sleep(300)

            print(countcompany)
            time.sleep(20)
            handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
            driver.switch_to.window(handles[0])

            companyname=company["companyname"]
            try:
             companyurl=company["goodsurl"]
            except:
                continue
            print(companyname)
            print(companyurl)

            url =companyurl
            drivergood1 = driver

            #全部产品列表
            if url!=None and url.find("https://")!=-1:
               driver.get(url)
            else:
                continue
            time.sleep(2)

            try:
             closelogin = driver.find_element_by_id('sufei-dialog-close')
             closelogin.click()
            except:
                print(" closelogin")

            try:
             summaryPage = driver.page_source
             bs = BeautifulSoup(summaryPage, 'html.parser')
             # 分类
             if countcompanylogin == 0:
                 countcompanylogin+=1
                 logintab = bs.find(attrs={'id': '_oid_ifr_'})
                 if logintab != None:
                     time.sleep(1)
                     setClipboardText("")
                     setClipboardText("db1600800a640")
                     setClipboardText("db1600800a640")
                     execWhichStep3 = "1688产品/username_goodslist.action"
                     t3 = MouseActionExecute(execute_count=1, file_name=execWhichStep3)
                     t3.start()
                     t3.join()
                     time.sleep(1)
                     setClipboardText("9803320668a640")
                     execWhichStep = "1688产品/password_goodslist.action"
                     t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                     t2.start()
                     t2.join()
                     time.sleep(1)
                     execWhichStep = "1688产品/press_goodslist.action"
                     t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                     t2.start()
                     t2.join()
                     time.sleep(1)
             else:
                 countcompanylogin += 1

            except:
                print("no closelogin 2")
            time.sleep(10)
            summaryPage = drivergood1.page_source
            bs = BeautifulSoup(summaryPage, 'html.parser')
            #分类
            categoryul=""
            categorylis=""
            try:
             categoryul = bs.find(attrs={'class': 'wp-category-nav-list fd-clr'})
             categorylis = categoryul.find_all(attrs={'class': 'wp-category-list-item'})
            except:
                continue

            goods=[]

            iszhiwen=False
            zhiwenurl=""
            iszhineng=False
            zhinengurl=""
            for categoryli in categorylis:
                ahtml=categoryli.find('a')
                ahtmlurl=ahtml.get("href")
                ahtmltitle=ahtml.get_text()
                if ahtmltitle.find("指纹")!=-1:
                    if ahtmltitle.find("室内") == -1:
                      iszhiwen=True
                      zhiwenurl=ahtmlurl
                if ahtmltitle.find("智能")!=-1:
                    if ahtmltitle.find("室内")==-1:
                        iszhineng=True
                        zhinengurl=ahtmlurl



            if iszhiwen==True :
                goods+=getgoodlist(drivergood1,zhiwenurl)
            if iszhineng == True:
                goods+=getgoodlist(drivergood1, zhinengurl)
            company["goods"]=goods
            file2 = open("1688产品/智能锁工厂_产品.txt", "w+")
            w = file2.write(json.dumps(companys))
            file2.close()




def getgoodlist(adrivergood,url):
    handles = adrivergood.window_handles  # 获取当前窗口句柄集合（列表类型）
    adrivergood.switch_to.window(handles[0])



    goods = []
    adrivergood.get(url)
    time.sleep(2)
    try:
     closelogin = adrivergood.find_element_by_id('sufei-dialog-close')
     closelogin.click()
    except:
        print("no closelogin 3")
    summaryPage = adrivergood.page_source
    bs = BeautifulSoup(summaryPage, 'html.parser')
    listhtml = bs.find(attrs={'class': 'offer-list-row'})
    itemshtml = listhtml.find_all(attrs={'class': 'offer-list-row-offer'})

    for item in itemshtml:
        good = {}
        ahtml=item.find(attrs={'class': 'title-link'})
        aurl = ahtml.get("href")
        atitle = ahtml.get_text()
        orderhtml = item.find(attrs={'class': 'offer-order-container'})
        if orderhtml == None:
            continue
        ordervalue = orderhtml.get_text()
        #gooddetail = getlastpic2(aurl, adrivergood)
        goodpricehtml = item.find(attrs={'class': 'price-container'})
        lastimg_ulthtml=item.find(attrs={'class': 'image-list-ul fd-clr'})
        lastimg_lihtml=lastimg_ulthtml.find_all(attrs={'class': 'image-item'})
        lastpicurl=""
        if lastimg_lihtml!=None and len(lastimg_lihtml)>2:
         liimg=lastimg_lihtml[2].find(attrs={'class': 'image-item-summm'})
         lastpicurl = liimg.get("src")
        goodprice = goodpricehtml.get_text()
        good["title"] = atitle
        good["ordercount"] = ordervalue
        good["lastpicurl"] = lastpicurl
        good["price"] = goodprice
        goods.append(good)

    nextbtn=None
    try:
      nextbtn=adrivergood.find_element_by_class_name('next')
    except:
        nextbtn = None

    while nextbtn != None :
        time.sleep(20)
        handles = adrivergood.window_handles  # 获取当前窗口句柄集合（列表类型）
        adrivergood.switch_to.window(handles[0])

        nextbtn.click()

        try:
            nextbtn = adrivergood.find_element_by_class_name('next')
        except:
            nextbtn = None



        time.sleep(3)
        summaryPage = adrivergood.page_source
        bs = BeautifulSoup(summaryPage, 'html.parser')
        nextbtndisable = bs.find(attrs={'class': 'next-disabled'})
        listhtml = bs.find(attrs={'class': 'offer-list-row'})
        itemshtml = listhtml.find_all(attrs={'class': 'offer-list-row-offer'})
        for item in itemshtml:
            good = {}
            ahtml = item.find(attrs={'class': 'title-link'})
            aurl = ahtml.get("href")
            atitle = ahtml.get_text()
            orderhtml = item.find(attrs={'class': 'offer-order-container'})
            if orderhtml == None:
                continue
            ordervalue = orderhtml.get_text()
            # gooddetail = getlastpic2(aurl, adrivergood)
            goodpricehtml = item.find(attrs={'class': 'price-container'})
            lastimghtml = item.find(attrs={'class': 'image-item-summm'})
            lastpicurl = lastimghtml.get("src")
            goodprice = goodpricehtml.get_text()
            good["title"] = atitle
            good["ordercount"] = ordervalue
            good["lastpicurl"] = lastpicurl
            good["price"] = goodprice
            goods.append(good)
    return goods

def getlastpic(aurl,adriverpic):

    #cwd = getcwd()
    # 设置chrome驱动器
    #driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    #driver.set_page_load_timeout(2230)

    #driver.delete_all_cookies()

    time.sleep(3)
    url = aurl

    driverpic = adriverpic



    handles = driverpic.window_handles  # 获取当前窗口句柄集合（列表类型）
    driverpic.switch_to.window(handles[1])

    driverpic.get(url)


    try:
     closelogin = driverpic.find_element_by_id('sufei-dialog-close')
     closelogin.click()
     print("closelogin 4")
    except:
        print("no closelogin 4")

    summaryPage = driverpic.page_source
    bs = BeautifulSoup(summaryPage, 'html.parser')
    imgurl=''
    try:
     imghtml = driverpic.find_element_by_xpath('//*[@id="dt-tab"]/div/ul/li[5]/div/a/img')
     imgurl=imghtml.get_attribute("src")
    except:
        imgurl=''
        print('goodpic not catch')
    '''
    #是否有代发
    daifa=False
    daifahtml=bs.find(attrs={'class':'trade-type-menu-item active-type-for-consign active-type'})
    if daifahtml!=None:
        daifatext=daifahtml.get_text()
        if daifatext.find("代发")!=-1:
            ahtml = daifahtml.find('a')
            ahtmlurl = ahtml.get("href")
            daifa=True
            driverpic.get(ahtmlurl)
        else:
            

    if daifa==False:
        pricehtml=bs.find(attrs={'class': 'value price-length-6'})

        price='0'
        if pricehtml!=None:
            price=pricehtml.get_text()
        else:
            pricehtml = bs.find(attrs={'class': 'price - original - sku'})
            if pricehtml != None:
             price = pricehtml.get_text()
    else:

    '''
    #driverpic.quit()

    gooddetail={}
    gooddetail["imgurl"]=imgurl
    gooddetail["price"]=''


    return gooddetail


def getlastpic2(aurl, adriverpic):

    gooddetail = {}
    gooddetail["imgurl"] = ''
    gooddetail["price"] = ''

    return gooddetail


if __name__ == '__main__':
    goods()