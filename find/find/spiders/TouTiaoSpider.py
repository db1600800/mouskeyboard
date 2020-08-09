import hashlib
import os
import time
import requests
from selenium import webdriver
from os import getcwd, sep
from bs4 import BeautifulSoup
import json

global allmedia
allmedia = {}
global n
global m

#start_url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time='
#url = 'https://www.toutiao.com'

global ascp




headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
cookies = {'odin_tt': 'c45e25a1037bcc76acbb9618825211d1e832126fb733d9ab59c6f3b88fd724363101804f4ea3d81db0d895291b2b88e9377ca1bd7f77541ef8f3dc28571f2b16'}  # 此处cookies可从浏览器中查找，为了避免被头条禁止爬虫

max_behot_time = '0'   # 链接参数
title = []       # 存储新闻标题
source_url = []  # 存储新闻的链接
s_url = []       # 存储新闻的完整链接
source = []      # 存储发布新闻的公众号
media_url = {}   # 存储公众号的完整链接

def get_as_cp():  # 该函数主要是为了获取as和cp参数，程序参考今日头条中的加密js文件：home_4abea46.js
    zz = {}
    now = round(time.time())
    print(now) # 获取当前计算机时间
    e = hex(int(now)).upper()[2:] #hex()转换一个整数对象为16进制的字符串表示
    print('e:', e)
    a = hashlib.md5()  #hashlib.md5().hexdigest()创建hash对象并返回16进制结果
    print('a:', a)
    a.update(str(int(now)).encode('utf-8'))
    i = a.hexdigest().upper()
    print('i:', i)
    if len(e)!=8:
        zz = {'as':'479BB4B7254C150',
        'cp':'7E0AC8874BB0985'}
        return zz
    n = i[:5]
    a = i[-5:]
    r = ''
    s = ''
    for i in range(5):
        s= s+n[i]+e[i]
    for j in range(5):
        r = r+e[j+3]+a[j]
    zz ={
    'as':'A1'+s+e[-3:],
    'cp':e[0:3]+r+'E1'
    }
    print('zz:', zz)
    return zz

def getdata(url, headers, cookies):  # 解析网页函数
    r = requests.get(url, headers=headers, cookies=cookies)
    print(url)
    data = json.loads(r.text)
    return data






def inivalue():
        global allmedia
        global n
        media8 = open("tenxunmedia_" + str(n) + ".txt", 'r+', encoding='utf-8')
        filecontent = media8.read()
        allmedia = json.loads(filecontent)


if __name__ == '__main__':
        # getChapterUrl('http://ac.qq.com/Comic/ComicInfo/id/505435')
        # getChapterUrl('https://new.qq.com/omn/author/13030024')
        global gllmedia
        global n
        n = 0
        global m
        m = 0

        #inivalue()
        ascp=get_as_cp()

        ii = 13001294  # 13030024 13001294
        while True:
            stru = "https://lf-lq.snssdk.com/api/news/feed/v47/?"
            t1 = time.time()
            stru += "_rticket:"+str(int(t1))+"055"
            stru += "ab_client:a1%2Ce1%2Cf2%2Cg2%2Cf7"
            stru += "ab_feature:z1"
            stru += "ab_group:z2"
            stru += "ab_version:668905%2C1859937%2C668906%2C668908%2C668903%2C668904%2C668907%2C1906036%2C928942"
            stru += "abflag:3"
            stru += "ac:wifi"
            stru += "aid:35"
            stru += "app_name:news_article_lite"
            stru += "cached_item_num:0"
            stru += "category:news_local"
            stru += "cdid:a25fcaf1-e3c4-45ff-9d06-be74c194bffc"
            stru += "channel:lite_huawei"
            stru += "cid:79028425"
            stru += "city:%E5%B9%BF%E5%B7%9E%E5%B8%82"
            stru += "client_extra_params:%7B%22ad_download%22%3A%7B%22space_unoccupied%22%3A2239952%2C%22space_cleanable%22%3A0%7D%2C%22last_ad_position%22%3A-1%2C%22playparam%22%3A%22codec_type%3A0%22%7D"
            stru += "count:20"
            stru += "cp:5ff52a7b896a7q1" #+ ascp['cp']
            stru += "device_brand:HONOR"
            stru += "device_id:57590214805"
            stru += "device_platform:android"
            stru += "device_type:JSN-AL00"
            stru += "dpi:480"
            stru += "iid:4151352933755207"
            stru += "lac:9464"
            stru += "language:zh"
            stru += "last_ad_show_interval:-1"
            stru += "latitude:23.333581"
            stru += "loc_mode:7"
            t = time.time()
            stru += "min_behot_time:" + str(int(t))
            t = time.time()
            stru += "loc_time:" + str(int(t))

            stru += "last_refresh_sub_entrance_interval:" + str(int(t1))
            stru += "longitude:113.534046"
            stru += "mac_address:74%3AC1%3A4F%3A08%3A43%3AE3"
            stru += "manifest_version_code:7560"

            stru += "oaid:fe3ef6fd-fdef-ee9b-bffd-dfefb3f52f73"
            stru += "concern_id: 6216118373890132481"
            stru += "discard_cids:%5B1673873866476547%5D"
            stru += "openudid:f09934e470012ddb"
            stru += "os_api:29"
            stru += "os_version:10"
            stru += "plugin_enable:4"
            stru += "plugin_state:1417873092637"
            stru += "refer:1"
            stru += "refresh_reason:4"
            stru += "resolution:1080*2255"
            stru += "rom_version:emotionui_10.0.0_jsn-al00+10.0.0.166%28c00e70r1p4%29"
            stru += "sa_enable:0"
            stru += "ssmix:a"
            stru += "tma_jssdk_version:1.73.0.65"
            stru += "tt_from:click"
            stru += "update_version_code:75603"
            stru += "user_city:%E6%B9%9B%E6%B1%9F"
            stru += "version_code:756"
            stru += "version_name:7.5.6"
            url = stru
            # 当前进程的工作目录
            cwd = getcwd()
            # 设置chrome驱动器
            driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
            # 设置超时时间
            driver.set_page_load_timeout(123)

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
            if summaryObjContent == None or summaryObjContent == "" or summaryObjContent == []:
                print(url + '  404' + '\n')
                driver.quit()
                continue

            for i in range(len(summaryObjContent)):
                # 查找出一个a标签
                # aObj = summaryObjContent[i].find('a')
                # 查a标签的href值
                # href = aObj['href']
                # 标签<a>中含有其他标签，用k.get_text()
                # strip()方法，去除字符串开头或者结尾的空格
                # title = aObj.get_text().strip()

                title = summaryObjContent[i].text
                obj = {}
                obj["title"] = title
                obj["url"] = url
                allmedia[title] = obj

                print(title + ' url ' + url + '\n')

            if m != 0 and m % 50 == 0:
                fo = open("tenxunmedia_" + str(n) + ".txt", "w+")  # 存入文件中。。。
                fo.write(json.dumps(allmedia))
                fo.write('\n')
                fo.close()
                print(' 50 write file ' + '\n')

            if m % 2000 == 0:
                n += m // 2000
                print(' 2000  n :' + str(n) + '\n')

            if m % 2000 == 0:
                if m != 0:
                    allmedia = {}
            m += 1
            # 推出驱动并关闭所关联的所有窗口
            driver.quit()
