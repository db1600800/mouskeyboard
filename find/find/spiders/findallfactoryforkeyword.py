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

from pynput import keyboard, mouse
from pynput.keyboard import Controller as KeyBoardController, KeyCode
from pynput.mouse import Button, Controller as MouseController


def getsimilar():
      url = "https://factory.1688.com/zgc/page/ngkwxobr.html?__pageId__=98362&cms_id=98362&keywords=%E6%99%BA%E8%83%BD%E9%94%81"
      # 当前进程的工作目录
      cwd = getcwd()
      # 设置chrome驱动器
      driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
      # 设置超时时间
      driver.set_page_load_timeout(223000000)

      #cookies = driver.get_cookies()

      driver.delete_all_cookies()

      driver.get(url)
      driver.get(url)


      js = 'window.open("https://www.baidu.com");'  # 通过执行js，开启一个新的窗口
      driver.execute_script(js)

      js = 'window.open("https://www.baidu.com");'  # 通过执行js，开启一个新的窗口
      driver.execute_script(js)

      handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
      driver.switch_to.window(handles[0])


      time.sleep(5)
      summaryPage = driver.page_source
      bs = BeautifulSoup(summaryPage, 'html.parser')
      items = bs.find_all(attrs={'class': 'primary'})

      companys=[]
      #第一页一页20行
      for item in items:
         company={}
         title = item.find(attrs={'class': 'desc'})
         titlevalue=title.get_text()
         titleurl=title.get("href")
         company["companyname"]=titlevalue
         print(titlevalue)
         company["goodslisturl"] =""#getcompanygoodslisturl(titleurl, driver)
         company["companyurl"] = titleurl


         group_3 = item.find(attrs={'class': 'group_3'})
         mixinfos = group_3.find＿all(attrs={'class': 'mix-info'})
         count=0
         for mixinfo in mixinfos:
           if count==1:
             #合作客户
             hezuotitle = mixinfo.find(attrs={'class': 'txt_7'}).get_text()
             hezuovalue = mixinfo.find(attrs={'class': 'text_2'}).get_text()
             company["hezuocount"]=hezuovalue
           if count==2:
              #回头率
              huitoutitle = mixinfo.find(attrs={'class': 'txt_7'}).get_text()
              huitouvalue = mixinfo.find(attrs={'class': 'text_2'}).get_text()
              company["huitou"] = huitouvalue.replace("%","")
           if count==3:
              #有意向
              yixiangtitle = mixinfo.find(attrs={'class': 'txt_7'}).get_text()
              yixiangvalue = mixinfo.find(attrs={'class': 'text_2'}).get_text()
              company["yixiang"] = yixiangvalue.replace("人","")
           count+=1
         companys.append(company)

      nextbtn=None
      handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
      driver.switch_to.window(handles[0])
      nextbtn = driver.find_element_by_class_name("next")


      countpage=1
      while nextbtn!=None and nextbtn.is_enabled()==True:
          if countpage>99:
              break
          handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
          driver.switch_to.window(handles[0])
          nextbtn=driver.find_element_by_class_name("next")


          nextbtn.click()

          time.sleep(2)
          summaryPage = driver.page_source


          bs = BeautifulSoup(summaryPage, 'html.parser')
          items = bs.find_all(attrs={'class': 'primary'})
          # 公司列表 第n页一页20行
          for item in items:
              company = {}
              title = item.find(attrs={'class': 'desc'})
              titlevalue = title.get_text()
              titleurl = title.get("href")
              company["companyname"] = titlevalue
              print(titlevalue)
              company["goodslisturl"]=""#getcompanygoodslisturl(titleurl,driver)
              company["companyurl"]=titleurl
              #company["goods"] = company["goods"]+goods(titleurl,driver)

              group_3 = item.find(attrs={'class': 'group_3'})
              mixinfos = group_3.find＿all(attrs={'class': 'mix-info'})
              count = 0
              for mixinfo in mixinfos:
                  if count == 1:
                      # 合作客户
                      hezuotitle = mixinfo.find(attrs={'class': 'txt_7'}).get_text()
                      hezuovalue = mixinfo.find(attrs={'class': 'text_2'}).get_text()
                      company["hezuocount"] = hezuovalue
                  if count == 2:
                      # 回头率
                      huitoutitle = mixinfo.find(attrs={'class': 'txt_7'}).get_text()
                      huitouvalue = mixinfo.find(attrs={'class': 'text_2'}).get_text()
                      company["huitou"] = huitouvalue.replace("%", "")
                  if count == 3:
                      # 有意向
                      yixiangtitle = mixinfo.find(attrs={'class': 'txt_7'}).get_text()
                      yixiangvalue = mixinfo.find(attrs={'class': 'text_2'}).get_text()
                      company["yixiang"] = yixiangvalue.replace("人", "")
                  count += 1
              companys.append(company)
              file2 = open("1688产品/智能锁工厂.txt", "w+")
              w = file2.write(json.dumps(companys))
              file2.close()
          countpage+=1





def getcompanygoodslisturl(titleurl,driver):
    '''
    area1_xiaoqufile = open("1688产品/智能锁工厂.txt", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    companys = json.loads(filecontent)


    cwd = getcwd()
    # 设置chrome驱动器
    driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    driver.set_page_load_timeout(2230)

    # cookies = driver.get_cookies()

    driver.delete_all_cookies()


    for company in companys:
        companyname = company["companyname"]
        titleurl = company["companyurl"]

    '''
    time.sleep(1)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    driver.switch_to.window(handles[1])

    url = titleurl


    drivergood = driver


    # 访问 公司主页
    drivergood.get(url)

    try:
        closelogin = drivergood.find_element_by_xpath('/html/body/div[5]/img')
        if closelogin!=None:
            time.sleep(1)

            setClipboardText("db1600800a640")
            execWhichStep = "1688产品/username.action"
            t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t2.start()
            t2.join()
            time.sleep(1)
            setClipboardText("9803320668a640")
            execWhichStep = "1688产品/password.action"
            t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t2.start()
            t2.join()
            time.sleep(1)
            execWhichStep = "1688产品/press.action"
            t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t2.start()
            t2.join()
            time.sleep(1)
        #closelogin.click()
    except:
        print("no closelogin 1")




    summaryPage = drivergood.page_source
    bs = BeautifulSoup(summaryPage, 'html.parser')
    shopurla = bs.find(attrs={'class': 'mod-info-footer-btn-white'})
    aurl = shopurla.get("href") + "/page/offerlist.htm"
    return aurl
    '''
    company["goodsurl"] = aurl
    print(companyname)
    print(aurl)

    file2 = open("1688产品/智能锁工厂goodsurl.txt", "w+")
    w = file2.write(json.dumps(companys))
    file2.close()
    '''


def getcompanygoodslisturl2():
    area1_xiaoqufile = open("1688产品/智能锁工厂.txt", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    companys = json.loads(filecontent)


    cwd = getcwd()
    # 设置chrome驱动器
    driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    driver.set_page_load_timeout(2230)

    # cookies = driver.get_cookies()

    driver.delete_all_cookies()

    for company in companys:
        companyname = company["companyname"]
        titleurl = company["companyurl"]


        time.sleep(1)
    #handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    #driver.switch_to.window(handles[1])

        url = titleurl


        drivergood = driver


        # 访问 公司主页
        drivergood.get(url)
        time.sleep(1)
        try:

            closelogin = drivergood.find_element_by_xpath('/html/body/div[5]/img')


            if closelogin != None:
                time.sleep(1)


                setClipboardText("db1600800a640")
                execWhichStep3 = "1688产品/username.action"
                t3 = MouseActionExecute(execute_count=1, file_name=execWhichStep3)
                t3.start()
                t3.join()
                time.sleep(1)
                setClipboardText("9803320668a640")
                execWhichStep = "1688产品/password.action"
                t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t2.start()
                t2.join()
                time.sleep(1)
                execWhichStep = "1688产品/press.action"
                t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t2.start()
                t2.join()
                time.sleep(1)
            #closelogin.click()
        except:
            print("no closelogin 1")

        time.sleep(2)
        summaryPage = drivergood.page_source
        bs = BeautifulSoup(summaryPage, 'html.parser')
        shopurla = bs.find(attrs={'class': 'mod-info-footer-btn-white'})
        if shopurla!=None:
            aurl = shopurla.get("href") + "/page/offerlist.htm"
        #return aurl

            company["goodsurl"] = aurl
            print(companyname)
            print(aurl)

            file2 = open("1688产品/智能锁工厂goodsurl.txt", "w+")
            w = file2.write(json.dumps(companys))
            file2.close()


if __name__ == '__main__':
    #getsimilar()
    getcompanygoodslisturl2()