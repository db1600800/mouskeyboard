import json
import random
import os
import re
import pypinyin
from qqkeyboard_sendmsg import *

def sendMsgToG(startExecuteBtn):
    global execWhichStep
    area1_xiaoqufile = open("area_page2.json", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    partOneObjs = json.loads(filecontent)
    citys = partOneObjs.keys()
    #citys=['惠州']
    # page1 citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']
    #citys = ['佛山']
    # page3 dict_keys(['扬州', '淄博', '珠海', '舟山', '威海', '中山', '郑州', '镇江', '漳州', '湛江', '岳阳', '银川', '徐州', '烟台', '厦门', '西宁', '西安', '武汉', '芜湖', '无锡', '温州', '潍坊'])
    searchStr = ""
    requestAddStr = ""
    xiaoquDateAddCount = 30
    count = 0
    countquery = 0
    qqfobiden = 0
    for city in citys:
        countys = partOneObjs[city].keys()
        for county in countys:
            areas = partOneObjs[city][county].keys()
            for area in areas:
                xiaoqus = partOneObjs[city][county][area].keys()
                for xiaoqu in xiaoqus:

                    xiaoqudict = partOneObjs[city][county][area][xiaoqu]
                    if xiaoqudict.get("isRequestQQGroup") == True:
                        xiaoquname = xiaoqudict["xiaoquname"]
                        href = xiaoqudict["href"]
                        address = xiaoqudict["address"]
                        dong = xiaoqudict["dong"]
                        fengqi = xiaoqudict["fengqi"]

                        searchXiaoquStr=""
                        xiaoqunameleftright = xiaoquname.split("·")
                        if len(xiaoqunameleftright) > 1:
                            searchXiaoquStr=xiaoqunameleftright[1]
                        else:
                            searchXiaoquStr = xiaoquname

                        msg=getMsg(city,county,area,xiaoqu)
                        if msg==None or msg=="":
                            continue
                        title=msg.split(".html")

                        titlepin = pypinyin.pinyin(msg, style=pypinyin.FIRST_LETTER)
                        titlestr = ""
                        i = 1
                        for t in titlepin:
                            if len(titlepin) > 10 and i < 10:
                                titlestr += t[0]
                            elif len(titlepin) <= 10 and i < len(titlepin):
                                titlestr += t[0]
                            i += 1


                        citypin = pypinyin.lazy_pinyin(city)
                        citystr = ""
                        for p in citypin:
                            citystr += p[0]
                        date = time.strftime("%Y%m%d", time.localtime())
                        msgStr=title[0]+"http://39.103.151.127:8080/"+str(date)+"/"+citystr+"/"+titlestr+".html"
                        print(msgStr)

                        setClipboardText(searchXiaoquStr)
                        execWhichStep = "向群发消息脚本/1选中搜索框并粘贴搜索.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t3 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t3.start()
                        t3.join()

                        time.sleep(2)

                        execWhichStep = "向群发消息脚本/2选择第一个.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t21 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t21.start()
                        t21.join()
                        time.sleep(2)

                        setClipboardText(msgStr)
                        execWhichStep = "向群发消息脚本/3粘贴消息到群.txt"
                        startExecuteBtn['text'] = execWhichStep
                        t31 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t31.start()
                        t31.join()


                        time.sleep(1)

                        execWhichStep = "向群发消息脚本/4发送.txt"
                        startExecuteBtn['text'] = execWhichStep
                        t32 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t32.start()
                        t32.join()
                        cell1Str = getClipboardText()
                        print(cell1Str)
                        print("send 4发送完成")

                        time.sleep(20)



    area1_xiaoqufile.close()




def list_all_files(rootdir):
    import os
    _files = []

    # 列出文件夹下所有的目录与文件

    list_file = os.listdir(rootdir)

    for i in range(0, len(list_file)):

        # 构造路径
        path = os.path.join(rootdir, list_file[i])

        # 判断路径是否是一个文件目录或者文件
        # 如果是文件目录，继续递归

        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files





def getMsg(city,county,area,xiaoquname):

    searchXiaoquName = ""
    xiaoqunameleftright = xiaoquname.split("·")
    if len(xiaoqunameleftright) > 1:
        searchXiaoquName = xiaoqunameleftright[1]
    else:
        searchXiaoquName = xiaoquname


    xiaoqugroup=[]
    areagroup=[]
    countygroup=[]

    citygroup=[]

    oldgroup=[]
    studygroup = []
    surprisegroup = []
    travelgroup = []
    eatgroup = []
    knowledgegroup=[]
    otherGroup=[]

    if xiaoqugroup!=[]:
        return  xiaoqugroup[random.randint(0, len(xiaoqugroup)-1)]

    # 1
    oldgroupkey = []
    oldgroupkey.append("旧影")
    oldgroupkey.append("老照片")
    oldgroupkey.append("历史照片")
    oldgroupkey.append("回忆")
    oldgroupkey.append("被遗忘")
    oldgroupkey.append("史上")

    studykey = []
    studykey.append("读书")
    studykey.append("考入")
    studykey.append("状元")
    studykey.append("名校")
    studykey.append("学校")


    surprisekey = []
    surprisekey.append("新奇古怪")
    surprisekey.append("大客机")
    surprisekey.append("怎么回事")
    surprisekey.append("百思")
    surprisekey.append("现场")
    surprisekey.append("土豪回老家")
    surprisekey.append("最奇葩")


    travelkey = []
    travelkey.append("旅游")
    travelkey.append("风土人情")
    travelkey.append("历史文化")
    travelkey.append("印象")
    travelkey.append("手绘地图")
    travelkey.append("游客")
    travelkey.append("卫星")
    travelkey.append("海景")
    travelkey.append("夜景")
    travelkey.append("故居")

    eatkey = []
    eatkey.append("吃")
    eatkey.append("香喷喷")
    eatkey.append("味道")
    eatkey.append("好极了")
    eatkey.append("新吃法")
    eatkey.append("香味")
    eatkey.append("吃的过瘾")
    eatkey.append("小吃")
    eatkey.append("好吃")


    knowledgekey = []
    knowledgekey.append("新知识")
    knowledgekey.append("你知道")
    knowledgekey.append("为什么")
    knowledgekey.append("崛起")

    date = time.strftime("%Y%m%d", time.localtime())
    shouhumediasrc_dir = r'../touxiaoHtml/'+date+'/'+city+''  # 源文件目录地址
    if os.path.exists(shouhumediasrc_dir) == False:
        return ""
    files = list_all_files(shouhumediasrc_dir)

    #分组
    for filepath in files:
        filename = os.path.basename(filepath)

        if check_contain_chinese(filename)==True:

            if filename.find(xiaoquname)!=-1:
                xiaoqugroup.append(filename)
            elif filename.find(area)!=-1:
                areagroup.append(filename)
            elif filename.find(county)!=-1:
                countygroup.append(filename)
            elif filename.find(city)!=-1:
                citygroup.append(filename)
            else:
                otherGroup.append(filename)



            for oldkey in oldgroupkey:
                if filename.find(oldkey)!=-1:
                     oldgroup.append(filename)
                     break

            #2

            for key in studykey:
                if filename.find(key)!=-1:
                     studygroup.append(filename)
                     break

            #3

            for key in surprisekey:
                if filename.find(key)!=-1:
                     surprisegroup.append(filename)
                     break

            #4
            for key in knowledgekey:
                if filename.find(key)!=-1:
                     knowledgegroup.append(filename)
                     break


            #5

            for key in travelkey:
                if filename.find(key)!=-1:
                     travelgroup.append(filename)
                     break

            #7

            for key in eatkey:
                if filename.find(key)!=-1:
                     eatgroup.append(filename)
                     break

    if xiaoqugroup!=[]:
        return  xiaoqugroup[random.randint(0, len(xiaoqugroup)-1)]
    elif areagroup!=[]:
        return  areagroup[random.randint(0, len(areagroup)-1)]
    elif countygroup!=[]:
        return  countygroup[random.randint(0, len(countygroup)-1)]
    elif otherGroup!=[]:
        return  otherGroup[random.randint(0, len(otherGroup)-1)]


    return ""


def check_contain_chinese(check_str):
      for ch in check_str:
          if u'\u4e00' <= ch <= u'\u9fff':
             return True
      return False