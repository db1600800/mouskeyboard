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
    updownnoper=updownvalue/float(buyvaluenum)
    updownper="%.2f%%" % (updownvalue/float(buyvaluenum) * 100)

    #涨了百分几
    jijingobj["updownperforbuy"]=updownper
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
       winmoney=float(buymoney)*updownnoper-float(buymoney)*0.0015-(float(buymoney)+float(buymoney)*updownnoper)*float(sellperdown7)
       jijingobj["buyservicemoney"]=float(buymoney)*0.0015
       jijingobj["sellservicemoney"] = (float(buymoney)+float(buymoney)*updownnoper)*float(sellperdown7)
       jijingobj["winmoney"]=winmoney
    elif diff_business_days>=7:
         winmoney = float(buymoney) * updownnoper - float(buymoney) * 0.0015 - (float(buymoney)+float(buymoney)*updownnoper) * float(sellperup7)
         jijingobj["buyservicemoney"] = float(buymoney) * 0.0015
         jijingobj["sellservicemoney"] = (float(buymoney) + float(buymoney) * updownnoper) * float(sellperup7)
         jijingobj["winmoney"] = winmoney


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




    file2 = open("基金产品/"+idvalue+".html", "w+")
    w = file2.write(json.dumps(jijingobj))
    file2.close()






if __name__ == '__main__':
    id="217017"
    name="招商消费80ETF联接"
    aurl = 'http://fund.eastmoney.com/217017.html'
    abuyvaluenum = "2.71"
    abuydate = "2021-01-07"
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
    abuyvaluenum = "2.71"
    abuydate = "2021-01-07"
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