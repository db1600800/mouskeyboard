import os
import time
import requests
from selenium import webdriver
from lxml import etree
from os import getcwd,sep
from bs4 import BeautifulSoup

def getChapterUrl(url):
    headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        }
    part_url = "http://ac.qq.com"
    res = requests.get(url, headers=headers)
    html=res.content.decode()
    el = etree.HTML(html)
    li_list = el.xpath('//*[@id="chapter"]/div[2]/ol[1]/li')
    for li in li_list:
            for p in li.xpath("./p"):
                for span in p.xpath("./span[@class='works-chapter-item']"):
                    item = {}
                    list_title = span.xpath("./a/@title")[0].replace(' ', '').split('：')
                    if list_title[1].startswith(('第', '序')):
                        getChapterFile(part_url + span.xpath("./a/@href")[0], list_title[0],list_title[1])

def getChapterFile(url,path1,path2):
    #path = os.path.join(path)
    #漫画名称目录
    path=os.path.join(path1)
    if not os.path.exists(path):
        os.mkdir(path)
    #章节目录
    path=path+'\\'+path2
    if not os.path.exists(path):
        os.mkdir(path)
    chrome=webdriver.Chrome()
    #"http://ac.qq.com/ComicView/index/id/505435/cid/2"
    chrome.get(url)
    time.sleep(4)
    imgs = chrome.find_elements_by_xpath("//div[@id='mainView']/ul[@id='comicContain']//img")
    for i in range(0, len(imgs)):
            js="document.getElementById('mainView').scrollTop="+str((i) * 1280)
            chrome.execute_script(js)
            time.sleep(3)
            print(imgs[i].get_attribute("src"))
            with open(path+'\\'+str(i)+'.png', 'wb') as f:
                f.write(requests.get(imgs[i].get_attribute("src")).content)
    chrome.close()
    print('下载完成')

if __name__ == '__main__':
    #getChapterUrl('http://ac.qq.com/Comic/ComicInfo/id/505435')
    #getChapterUrl('https://new.qq.com/omn/author/13030024')
    ii=0 #13030024
    while True:
        url='https://new.qq.com/omn/author/'+str(ii)
        # 当前进程的工作目录
        cwd = getcwd()
        # 设置chrome驱动器
        driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
        # 设置超时时间
        driver.set_page_load_timeout(13)

        # 访问
        driver.get(url)
        # 等待几秒
        #time.sleep(3)

        # 清空文本框的内容
        #driver.find_element_by_name('word').clear()
        # 输入文本内容
        #driver.find_element_by_name('word').send_keys('百度')
        # 点击按钮
        #driver.find_element_by_id("s_btn_wr").click()
        ii += 1
        # 获得网页内容
        summaryPage = driver.page_source
        # 解析HTML内容
        summaryObj = BeautifulSoup(summaryPage, 'html.parser')
        # 通过Class获取内容
        summaryObjContent = summaryObj.find_all(attrs={'class': 'author-name'})
        if summaryObjContent==None or summaryObjContent=="":
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
            print(title + '\n'  + '\n')


        # 推出驱动并关闭所关联的所有窗口
        driver.quit()
