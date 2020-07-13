import scrapy
import re
import time
import json

class StocksSpider(scrapy.Spider):
    name = "stocks"

    global allxiaoqu
    allxiaoqu={}


    def start_requests(self):
        urls = [
            'https://gz.newhouse.fang.com/house/s/'
        ]
        for url in urls:
           yield scrapy.Request(url=url, callback=self.parse_city12)
           #yield scrapy.Request(url=url,callback=lambda response, pcity="广州": self.parse_area(response, pcity))
           """
           yield scrapy.Request(url=url, callback=lambda response, areaurl=url, pcity="广州",
                                                             pquyuname="增城": self.parse_area_chirld(response,
                                                                                                        areaurl, pcity,
                                                                                                        pquyuname))
           """

    def parse(self, response,city,quyu,quyuchirld):
        pcity=city
        pquyu=quyu
        pquyuchirld=quyuchirld

        if allxiaoqu.get(pcity)==None:
              allxiaoqu[pcity]={}
        if allxiaoqu[pcity].get(pquyu)==None:
              allxiaoqu[pcity][pquyu]={}
        if pquyuchirld!="" and allxiaoqu[pcity][pquyu].get(pquyuchirld)==None:
            allxiaoqu[pcity][pquyu][pquyuchirld]={}


        names=response.css('.nlcd_name a::text').extract()
        hrefs=response.css('.nlcd_name a::attr(href)').extract()
        addrs=response.css('.address a::text').extract()

        iii=0
        for namee in names:
            name=namee.strip()
            if pquyuchirld!="":
                if allxiaoqu[pcity][pquyu][pquyuchirld].get(name)==None :
                  allxiaoqu[pcity][pquyu][pquyuchirld][name]={}
                else:
                    v=0
                allxiaoqu[pcity][pquyu][pquyuchirld][name]["xiaoquname"]=name.strip()
                allxiaoqu[pcity][pquyu][pquyuchirld][name]["href"] = "https:" + hrefs[iii]
                allxiaoqu[pcity][pquyu][pquyuchirld][name]["address"] = addrs[iii].strip()
            else:
              if allxiaoqu[pcity][pquyu].get(name) == None :
                allxiaoqu[pcity][pquyu][name] ={}
              else:
                 v=0
              allxiaoqu[pcity][pquyu][name]["xiaoquname"] = name.strip()
              allxiaoqu[pcity][pquyu][name]["href"] = "https:" + hrefs[iii]
              allxiaoqu[pcity][pquyu][name]["address"] = addrs[iii].strip()

            yield scrapy.Request(url="https:" + hrefs[iii], callback=lambda response, xcity=pcity, xquyu=pquyu,
                                                                      xquyuchirld=pquyuchirld,
                                                                      xxiaoqukey=name: self.parse_xiaoqu_detail(
                response,
                xcity,
                xquyu,
                xquyuchirld, xxiaoqukey))
            time.sleep(1)
            iii += 1

        nexthref=response.css('.next::attr(href)').extract()
        if nexthref==[]:
            fo = open("filefile1.txt", "w+")  # 存入文件中。。。
            fo.write(json.dumps(allxiaoqu))
            fo.write('\n')
            fo.close()
        else:
           for pagehref in nexthref:
                 preurl = response.url.split("/")[2]
                 nexturl="https://"+preurl+pagehref
                 yield scrapy.Request(url=nexturl, callback=lambda response, city=pcity, quyu=pquyu,
                                                                   quyuchirld=pquyuchirld: self.parse(response,
                                                                                                          city, quyu,
                                                                                                          quyuchirld))
                 time.sleep(1)



    def parse_xiaoqu_detail(self, response,xcity,xquyu,xquyuchirld,xxiaoqukey):
        dongs = response.css('#dong_1期 span::text').extract()
        fengqi = response.css('.chldper li::text').extract()

        dongstr = ""
        for dong in dongs:
            dongstr += dong + ","

        if xquyuchirld != "":
            allxiaoqu[xcity][xquyu][xquyuchirld][xxiaoqukey]["dong"] = dongstr
            if fengqi == []:
                allxiaoqu[xcity][xquyu][xquyuchirld][xxiaoqukey]["fengqi"] = "false"
            else:
                allxiaoqu[xcity][xquyu][xquyuchirld][xxiaoqukey]["fengqi"] = "true"
        else:
            allxiaoqu[xcity][xquyu][xxiaoqukey]["dong"] = dongstr
            if fengqi == []:
              allxiaoqu[xcity][xquyu][xxiaoqukey]["fengqi"] = "false"
            else:
              allxiaoqu[xcity][xquyu][xxiaoqukey]["fengqi"] = "true"



    def parse_city11(self, response):
        quyu_name_hrefs = response.css('#cityi011 a::attr(href)').extract()
        quyu_names = response.css('#cityi011 a::text').extract()
        ii = 0
        for href in quyu_name_hrefs:
            if href != "#no" and quyu_names[ii]!="更多":
                quyuurl = href
                quyuname = quyu_names[ii]
                yield scrapy.Request(url=quyuurl,
                                     callback=lambda response, pcity=quyuname: self.parse_area(response,
                                                                                               pcity))
                time.sleep(1)
            ii += 1

    def parse_city12(self, response):
        quyu_name_hrefs = response.css('#cityi012 a::attr(href)').extract()
        quyu_names = response.css('#cityi012 a::text').extract()
        ii = 0
        for href in quyu_name_hrefs:
            if href != "#no" and quyu_names[ii]!="更多":
                quyuurl =  href
                quyuname = quyu_names[ii]
                yield scrapy.Request(url=quyuurl,
                                     callback=lambda response, pcity=quyuname: self.parse_area(response,
                                                                                               pcity))
                time.sleep(1)
            ii += 1

    def parse_city13(self, response):
        quyu_name_hrefs = response.css('#cityi013 a::attr(href)').extract()
        quyu_names = response.css('#cityi013 a::text').extract()
        ii = 0
        for href in quyu_name_hrefs:
            if href != "#no" and quyu_names[ii]!="更多":
                quyuurl =  href
                quyuname = quyu_names[ii]
                yield scrapy.Request(url=quyuurl,
                                     callback=lambda response, pcity=quyuname: self.parse_area(response,
                                                                                                          pcity))
                time.sleep(1)
            ii += 1



    def parse_area(self, response,pcity):
        quyu_name_hrefs = response.css('#quyu_name a::attr(href)').extract()
        quyu_names = response.css('#quyu_name a::text').extract()
        ii=0
        for href in quyu_name_hrefs:
             if href!="#no":
                preurl=response.url.split("/")[2]
                quyuurl = "https://"+preurl + href
                quyuname=quyu_names[ii]
                yield scrapy.Request(url=quyuurl, callback=lambda response,areaurl=quyuurl,pcity=pcity, pquyuname=quyuname:self.parse_area_chirld(response,areaurl,pcity,pquyuname))
                time.sleep(1)
             ii += 1

    def parse_area_chirld(self, response,areaurl,pcity,pquyuname):
        quyu_chirld_name_hrefs = response.css('.quyu a::attr(href)').extract()
        quyu_chirld_names = response.css('.quyu a::text').extract()
        if quyu_chirld_name_hrefs==[]:
            yield scrapy.Request(url=areaurl, callback=lambda response, city=pcity, quyu=pquyuname,
                                                                    quyuchirld="": self.parse(response,city, quyu,quyuchirld))
            time.sleep(1)
        else:
         ii=0
         for href in quyu_chirld_name_hrefs:
             if href!="#no":
                preurl = response.url.split("/")[2]
                quyuchirldurl = "https://"+preurl + href
                quyuchirldname=quyu_chirld_names[ii]
                yield scrapy.Request(url=quyuchirldurl, callback=lambda response, city=pcity,quyu=pquyuname,quyuchirld=quyuchirldname:self.parse(response,city,quyu,quyuchirld))
                time.sleep(1)
             ii+=1