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
import datetime
from dateutil import rrule



def goods(aurl,
    abuyvaluenum,
    abuydate,
    abuymoney,
    asellperdown7,
    asellperup7):

    cwd = getcwd()
    # 设置chrome驱动器
    driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
    # 设置超时时间
    driver.set_page_load_timeout(2230)

    # cookies = driver.get_cookies()

    driver.delete_all_cookies()

    url=aurl
    buyvaluenum=abuyvaluenum
    buydate=abuydate
    buymoney=abuymoney
    #赎回费率小于7天 1.5%
    sellperdown7=asellperdown7
    #赎回费率大于等于7天 0.5%
    sellperup7=asellperup7


    driver.get(url)



    time.sleep(5)
    js1 = 'document.querySelector("#hq_ip_tips > div.ip_tips_layer.layer2 > div > span").click()'

    driver.execute_script(js1)


    time.sleep(5)


    jijingobj={}

    summaryPage = driver.page_source
    bs = BeautifulSoup(summaryPage, 'html.parser')
    driver.close()

    valueper = bs.find(attrs={'id': 'gz_gszzl'})
    updown=valueper.get_text()
    #比上一交易日涨了多少
    jijingobj["updownperforyesterdate"]=updown

    timenow = bs.find(attrs={'id': 'gz_gztime'})
    timevalue = timenow.get_text()
    #当前日期
    jijingobj["time"]=timevalue

    valuenum = bs.find(attrs={'id': 'gz_gsz'}).get_text()
    jijingobj["valuenum"]=valuenum
    updownvalue=float(valuenum)-float(buyvaluenum)
    updownnoperforbuy=updownvalue/float(buyvaluenum)
    updownperforbuy="%.2f%%" % (updownvalue/float(buyvaluenum) * 100)

    #离买的时候涨了百分几
    jijingobj["updownperforbuy"]=updownperforbuy
    #买的时候多少钱
    jijingobj["buyvaluenum"]=buyvaluenum
    #买的时候日期
    jijingobj["buydate"]=buydate


    #买了几天 不包括周六周日
    buyDateObj = time.strptime(buydate, '%Y-%m-%d')
    nowDateObj = time.strptime(timevalue, '%Y-%m-%d %H:%M')

    buya = datetime.datetime(buyDateObj.tm_year, buyDateObj.tm_mon, buyDateObj.tm_mday)
    nowb = datetime.datetime(nowDateObj.tm_year, nowDateObj.tm_mon, nowDateObj.tm_mday)

    diff_business_days = len(list(rrule.rrule(rrule.DAILY,
                                               dtstart=buya,
                                               until=nowb - datetime.timedelta(days=1),
                                               byweekday=(rrule.MO, rrule.TU, rrule.WE, rrule.TH, rrule.FR))))
    jijingobj["buydatenum"] = diff_business_days

    #赚了亏了多少
    if diff_business_days<7:
       buyservicemoney=float(buymoney)*0.0015
       jijingobj["buyservicemoney"]=buyservicemoney

       sellservicemoney=(float(buymoney)+float(buymoney)*updownnoperforbuy)*float(sellperdown7)
       jijingobj["sellservicemoney"] = sellservicemoney

       jijingobj["winmoney"]=float(buymoney)*updownnoperforbuy-buyservicemoney-sellservicemoney
    elif diff_business_days>=7:
        buyservicemoney = float(buymoney) * 0.0015
        jijingobj["buyservicemoney"] = buyservicemoney

        sellservicemoney = (float(buymoney) + float(buymoney) * updownnoperforbuy) * float(sellperup7)
        jijingobj["sellservicemoney"] = sellservicemoney

        jijingobj["winmoney"] = float(buymoney) * updownnoperforbuy - buyservicemoney - sellservicemoney



    id = bs.find(attrs={'class': 'ui-num'})
    idvalue = id.get_text()
    #基金代号
    jijingobj["id"]=idvalue



    title = bs.find(attrs={'class': 'fundDetail-tit'})
    titlevalue = title.get_text()
    #基金名称
    jijingobj["title"]=titlevalue

    for key, value in jijingobj.items():
       print('{key}:{value}'.format(key=key, value=value))

    comparehtml(jijingobj, idvalue,aurl)




def comparehtml(jijingobj,idvalue,aurl):

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
    for key, value in jijingobj.items():
     keycn=''
     if str(key)=='updownperforyesterdate':
         keycn='距离昨天上升多少'
     elif str(key) == 'time':
         keycn = '当前时间'
     elif str(key) == 'valuenum':
         keycn = '当前价格'
     elif str(key) == 'updownperforbuy':
         keycn = '距离买时上升多少'
     elif str(key) == 'buyvaluenum':
         keycn = '购买时价格'
     elif str(key) == 'buydate':
         keycn = '购买日期'
     elif str(key) == 'buydatenum':
         keycn = '购买了几天'
     elif str(key) == 'buyservicemoney':
         keycn = '购买服务费'
     elif str(key) == 'sellservicemoney':
         keycn = '卖掉服务费'
     elif str(key) == 'winmoney':
         keycn = '赚了多少'
     elif str(key) == 'id':
         keycn = '基金代码'
     elif str(key) == 'title':
         keycn = '基金名称'

     if str(key)=='title':
        html += '<tr><th>'+str(keycn)+'</th><th><a href="'+aurl+'">'+str(value)+'</a></th></tr>\n'
     else:
         html += '<tr><th>' + str(keycn) + '</th><th>' + str(value) + '</th></tr>\n'

    html += '</table>\n'
    html += '</html>\n'

    file2 = open("基金产品/"+idvalue+".html", "w+")
    w = file2.write(html)
    file2.close()



if __name__ == '__main__':
    while True:
        id="217017"
        name="招商消费80ETF联接"
        aurl = 'http://fund.eastmoney.com/217017.html'
        abuyvaluenum = "3.0785"
        abuydate = "2021-01-20"
        abuymoney = "40000"
        # 赎回费率小于7天 1.5%
        asellperdown7 = "0.015"
        # 赎回费率大于等于7天 0.5%
        asellperup7 = "0.005"

        goods(aurl,
        abuyvaluenum,
        abuydate,
        abuymoney,
        asellperdown7,
        asellperup7)






        id = "001245"
        name = "工银瑞信生态环境股票"
        aurl = 'http://fund.eastmoney.com/001245.html'
        abuyvaluenum = "1.913"
        abuydate = "2021-01-20"
        abuymoney = "39000"
        # 赎回费率小于7天 1.5%
        asellperdown7 = "0.015"
        # 赎回费率大于等于7天 0.5%
        asellperup7 = "0.0075"

        goods(aurl,
              abuyvaluenum,
              abuydate,
              abuymoney,
              asellperdown7,
              asellperup7)

        time.sleep(60)