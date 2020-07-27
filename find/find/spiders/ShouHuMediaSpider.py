import scrapy
import re
import time
import json
import random

class ShouHuMediaSpider(scrapy.Spider):
    name = "shouhumediaspider"

    global allmedia
    allmedia={}
    global allxiaoqu
    allxiaoqu={}
    global i
    i=0


    def inivalue(self):
        global allmedia
        media8 = open("shouhumedia8_" + str(2) + ".txt", 'r+', encoding='utf-8')
        filecontent = media8.read()
        allmedia = json.loads(filecontent)

    def start_requests(self):
        self.inivalue()


        ii =20229465 #20125864 #1000 25783 100000 20122456  120229465
        global i
        global allmedia
        m = 0
        if allmedia!={}:
            m= len(allmedia)

        n=5

        urls = [
            'https://m.sohu.com/media/1'
        ]
        #120053275
        #124706


        while True:
            if i >99:
                i = 0
                if len(str(ii)) == 3:
                    fo = open("shouhumedia3.txt", "w+")  # 存入文件中。。。
                    fo.write(json.dumps(allmedia))
                    fo.write('\n')
                    fo.close()
                elif len(str(ii)) == 4:
                        fo = open("shouhumedia4.txt", "w+")  # 存入文件中。。。
                        fo.write(json.dumps(allmedia))
                        fo.write('\n')
                        fo.close()
                elif len(str(ii)) == 5:
                    fo = open("shouhumedia5.txt", "w+")  # 存入文件中。。。
                    fo.write(json.dumps(allmedia))
                    fo.write('\n')
                    fo.close()
                elif len(str(ii)) == 6:
                    fo = open("shouhumedia6.txt", "w+")  # 存入文件中。。。
                    fo.write(json.dumps(allmedia))
                    fo.write('\n')
                    fo.close()
                elif len(str(ii))==7:
                   fo = open("shouhumedia7.txt", "w+")  # 存入文件中。。。
                   fo.write(json.dumps(allmedia))
                   fo.write('\n')
                   fo.close()
                elif len(str(ii)) == 8:
                    fo = open("shouhumedia8_" + str(n) + ".txt", "w+")  # 存入文件中。。。
                    fo.write(json.dumps(allmedia))
                    fo.write('\n')
                    fo.close()

                    if m%20000==0:
                        n+=m//20000

                    if m % 20000 == 0:
                      if m!=0:
                        allmedia={}
                    m+=100


            if len(str(ii)) == 9:
                break
            url = urls[0] + str(ii)
            yield scrapy.Request(url=url, callback=self.parse_city11)
            ii+=1
            time.sleep(0.1)
           #yield scrapy.Request(url=url,callback=lambda response, pcity="广州": self.parse_area(response, pcity))
            """
             yield scrapy.Request(url=url, callback=lambda response, areaurl=url, pcity="广州",
                                                             pquyuname="增城": self.parse_area_chirld(response,
                                                                                                        areaurl, pcity,
                                                                                                        pquyuname))
            """



    def parse_city11(self, response):
        global allmedia
        url=response.url
        if url.find("404")!=-1:
            print("not find page")
        else:
            titles = response.css('.ai_con_head_ins_title::text').extract()
            if titles!=None and titles!=[]:
                title=titles[0]
                obj={}
                obj["title"]=title
                obj["url"]=url
                allmedia[title]=obj
                global i
                i+=1
                print(title)






