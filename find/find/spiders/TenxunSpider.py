
from selenium import webdriver
from os import getcwd,sep
from bs4 import BeautifulSoup
import json



if __name__ == '__main__':
    #getChapterUrl('http://ac.qq.com/Comic/ComicInfo/id/505435')
    #getChapterUrl('https://new.qq.com/omn/author/13030024')
    allmedia={}
    n=0
    m=0
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
            obj = {}
            obj["title"] = title
            obj["url"] = url
            allmedia[title] = obj

            print(title + '\n'  + '\n')

        if m!=0 and m%50==0:
            fo = open("tenxunmedia_" + str(n) + ".txt", "w+")  # 存入文件中。。。
            fo.write(json.dumps(allmedia))
            fo.write('\n')
            fo.close()

        if m % 2000 == 0:
            n += m // 2000

        if m % 2000 == 0:
            if m != 0:
                allmedia = {}
        m+=1
        # 推出驱动并关闭所关联的所有窗口
        driver.quit()
