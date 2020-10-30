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


def getsimilar():

  try:
      url = "https://factory.1688.com/zgc/page/ngkwxobr.html?__pageId__=98362&cms_id=98362&keywords=%E6%99%BA%E8%83%BD%E9%94%81"
      # 当前进程的工作目录
      cwd = getcwd()
      # 设置chrome驱动器
      driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
      # 设置超时时间
      driver.set_page_load_timeout(2230)

      #cookies = driver.get_cookies()

      driver.delete_all_cookies()

      # 访问
      driver.get(url)
      print(url)
      time.sleep(1)
      driver.get(url)
      time.sleep(2)
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
         company["goods"]=goods(titleurl)

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



      nextbtn = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div/button[2]")
      while nextbtn.is_enabled()==True:
          nextbtn.click()
          time.sleep(2)
          summaryPage = driver.page_source
          nextbtn = driver.find_element_by_xpath(
              "/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div/button[2]")
          bs = BeautifulSoup(summaryPage, 'html.parser')
          items = bs.find_all(attrs={'class': 'primary'})
          # 公司列表 第n页一页20行
          for item in items:
              company = {}
              title = item.find(attrs={'class': 'desc'})
              titlevalue = title.get_text()
              titleurl = title.get("href")
              company["companyname"] = titlevalue
              company["goods"] = company["goods"]+goods(titleurl)

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




  except Exception as e:
      y=0


def goods(aurl):

    url =aurl
    # 当前进程的工作目录
    cwd = getcwd()
    # 设置chrome驱动器
    drivergood = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    drivergood.set_page_load_timeout(2230)
    # cookies = driver.get_cookies()
    drivergood.delete_all_cookies()

    # 访问 公司主页
    drivergood.get(url)
    time.sleep(2)
    summaryPage = drivergood.page_source
    bs = BeautifulSoup(summaryPage, 'html.parser')
    shopurla = bs.find(attrs={'class': 'mod-info-footer-btn-white'})
    url = shopurla.get("href") + "/page/offerlist.htm"

    #全部产品列表
    drivergood.get(url)
    summaryPage = drivergood.page_source
    bs = BeautifulSoup(summaryPage, 'html.parser')
    #分类
    categoryul = bs.find(attrs={'class': 'wp-category-nav-list fd-clr'})
    categorylis = categoryul.find_all(attrs={'class': 'wp-category-list-item'})


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
            iszhiwen=True
            zhiwenurl=ahtmlurl
        if ahtmltitle.find("智能")!=-1:
            iszhineng=True
            zhinengurl=ahtmlurl
    if iszhiwen==True or iszhineng==True:
        #指纹
        drivergood.get(zhiwenurl)
        summaryPage = drivergood.page_source
        bs = BeautifulSoup(summaryPage, 'html.parser')
        listhtml = bs.find(attrs={'class': 'offer-list-row'})
        itemshtml = listhtml.find_all(attrs={'class': 'offer-list-row-offer'})

        for item in itemshtml:
            good = {}
            ahtml=item.find("a")
            aurl=ahtml.get("href")
            atitle=ahtml.get_text()
            orderhtml=item.find(attrs={'class': 'offer-order-container'})
            if orderhtml==None:
                continue
            ordervalue=orderhtml.get_text()
            gooddetail = getlastpic(aurl)
            lastpicurl = gooddetail["imgurl"]
            goodprice = gooddetail["price"]
            good["title"] = atitle
            good["ordercount"] = ordervalue
            good["lastpicurl"] = lastpicurl
            good["price"] = goodprice
            goods.append(good)

        nextbtn =bs.find(attrs={'class': 'next'})
        nextbtndisable = bs.find(attrs={'class': 'next-disabled'})

        while  nextbtn!=None and nextbtndisable==None:
            nextbtn.click()
            time.sleep(5)
            summaryPage = drivergood.page_source
            bs = BeautifulSoup(summaryPage, 'html.parser')
            nextbtndisable = bs.find(attrs={'class': 'next-disabled'})
            listhtml = bs.find(attrs={'class': 'offer-list-row'})
            itemshtml = listhtml.find_all(attrs={'class': 'offer-list-row-offer'})
            for item in itemshtml:
                ahtml = item.find("a")
                aurl = ahtml.get("href")
                atitle = ahtml.get_text()
                orderhtml = item.find(attrs={'class': 'offer-order-container'})
                ordervalue = orderhtml.get_text()
                gooddetail=getlastpic(aurl)
                lastpicurl = gooddetail["imgurl"]
                goodprice=gooddetail["price"]
                good["title"] = atitle
                good["ordercount"] = ordervalue
                good["lastpicurl"] = lastpicurl
                good["price"]=goodprice
                goods.append(good)

    drivergood.quit()
    return goods


def getlastpic(aurl):
    url = aurl
    # 当前进程的工作目录
    cwd = getcwd()
    # 设置chrome驱动器
    driverpic = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    driverpic.set_page_load_timeout(2230)
    # cookies = driver.get_cookies()
    driverpic.delete_all_cookies()

    # 访问 公司主页
    driverpic.get(url)
    time.sleep(2)
    summaryPage = driverpic.page_source
    bs = BeautifulSoup(summaryPage, 'html.parser')
    img = driverpic.find_element_by_xpath('//*[@id="dt-tab"]/div/ul/li[5]/div/a/img')
    imgurl=img.get('src')
    pricehtml=bs.find(attrs={'value price-length-6'})
    price=pricehtml.get_text()
    driverpic.quit()

    gooddetail={}
    gooddetail["imgurl"]=imgurl
    gooddetail["price"]=price
    return gooddetail


def comparehtml(pgoods,pfilename):

    html=''
    html += '<html>\n'
    html += '<script type="text/javascript">\n'
    html += '	window.onload=function(){\n'
    html += '	var tfrow = document.getElementById(\'tfhover\').rows.length;\n'
    html += '	var tbRow=[];\n'
    html += '	for (var i=1;i<tfrow;i++) {\n'
    html += '		tbRow[i]=document.getElementById(\'tfhover\').rows[i];\n'
    html += '		tbRow[i].onmouseover = function(){\n'
    html += '		  this.style.backgroundColor = \'#ffffff\';\n'
    html += '		};\n'
    html += '		tbRow[i].onmouseout = function() {\n'
    html += '		  this.style.backgroundColor = \'#d4e3e5\';\n'
    html += '		};\n'
    html += '	}\n'
    html += '};\n'
    html += '</script>\n'

    html += '<style type="text/css">\n'
    html += 'table.tftable {font-size:12px;color:#333333;width:100%;border-width: 1px;border-color: #729ea5;border-collapse:'
    html += 'collapse;}\n'
    html += 'table.tftable th {font-size:12px;background-color:#acc8cc;border-width: 1px;padding: 8px;border-style:solid;border-'
    html += 'color: #729ea5;text-align:left;}\n'
    html += 'table.tftable tr {background-color:#d4e3e5;}\n'
    html += 'table.tftable td {font-size:12px;border-width: 1px;padding: 8px;border-style: solid;border-color: #729ea5;}\n'
    html += '</style>\n'

    html += '<table id="tfhover" class="tftable" border="1">\n'
    for good in pgoods:
     title=good.get("title")
     imgurl=good.get("picurl")
     profit0="%.1f"%good.get("profit0")
     profit1 = "%.1f"%good.get("profit1")
     profit2 = "%.1f"%good.get("profit2")
     profit3 = "%.1f"%good.get("profit3")
     sellcount0=good.get("sellcount0")
     sellcount1 = good.get("sellcount1")
     sellcount2 = good.get("sellcount2")
     sellcount3 = good.get("sellcount3")
     url1688 = good.get("url1688")
     urltaobao = good.get("urltaobao")
     html += '<tr><th><a href="'+urltaobao+'"><img src="'+imgurl+'"></img></a></th><th><a href="'+url1688+'">'+title+'</a></th><th>'+profit0+'--'+str(sellcount0)+'</th><th>'+profit1+'--'+str(sellcount1)+'</th><th>'+profit2+'--'+str(sellcount2)+'</th><th>'+profit3+'--'+str(sellcount3)+'</th></tr>\n'

    html += '</table>\n'
    html += '</html>\n'

    file2 = open("1688产品/1688"+pfilename+".html", "w+")
    w = file2.write(html)
    file2.close()

if __name__ == '__main__':
    getsimilar()