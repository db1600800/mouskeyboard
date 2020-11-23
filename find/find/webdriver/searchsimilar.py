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

#第一步用这个tao1688.py  第二步用searchsimilar.py

def getsimilar():

    goods = []
    global execWhichStep
    filename="玩具"
    counti=0
    area1_xiaoqufile = open("1688产品/1688"+filename+".txt", 'r', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    level1item = json.loads(filecontent)
    for level2item in level1item.get('leve2'):
              for level2listitem in level2item[0].get('level2list'):
                      try:

                          item=level2listitem[0]
                          title1688=item["title"]
                          imgurl1688=item["imageurl"]
                          money1688=item["money"]
                          url1688=item["url"]
                          print(str(counti)+" "+title1688+imgurl1688)

                          filepath='C:\\a.jpg'


                          urllib.request.urlretrieve(imgurl1688, filename=filepath)


                          url = "https://www.taobao.com/"
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
                          time.sleep(5)

                          execWhichStep = "淘宝search/searchv1.txt"
                          t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                          t2.start()
                          t2.join()

                          time.sleep(15)

                          execWhichStep = "淘宝search/searchv2.txt"
                          t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                          t2.start()
                          t2.join()

                          time.sleep(5)
                          # 获得网页内容

                          summaryPage = driver.page_source
                          driver.quit()


                          # 解析HTML内容
                          bs = BeautifulSoup(summaryPage, 'html.parser')
                          listhtml = bs.find_all(attrs={'class': 'items g-clearfix'})
                          if listhtml==None or listhtml=='' or len(listhtml)!=1:
                              continue
                          items=listhtml[0].find_all(attrs={'class': 'item'})


                          good={}
                          count=0
                          for item in items:
                              if count>3:
                                  break
                              sellcount=item.find(attrs={'class': 'deal-cnt'}).get_text().replace('人付款','')
                              pricehtml = item.find_all(attrs={'class': 'price g_price g_price-highlight'})
                              price=pricehtml[0].find('strong').get_text()
                              lirun=float(price)-float(money1688)
                              a = item.find('a')
                              urltaobao=a.get("href")

                              good['profit'+str(count)]=lirun
                              good['title']=title1688
                              good['picurl']=imgurl1688
                              good['sellcount'+str(count)]=sellcount
                              good['url1688']=url1688
                              good['urltaobao']=urltaobao
                              count+=1
                          goods.append(good)

                          counti+=1
                          comparehtml(goods, filename)
                      except Exception as e:
                          continue
    file2 = open("1688产品/1688" + filename + ".json", "w+")
    file2.write(json.dumps(goods))
    file2.write('\n')
    file2.close()
    comparehtml(goods,filename)



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