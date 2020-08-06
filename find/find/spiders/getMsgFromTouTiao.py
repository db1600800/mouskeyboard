import json
import random
import os
import re
from qqkeyboard_getmsg import *

def getMsgFromToutiao(startExecuteBtn):
    global execWhichStep
    area1_xiaoqufile = open("area_page3.json", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    partOneObjs = json.loads(filecontent)
    citys = partOneObjs.keys()
    # citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']
    #citys = ['佛山']
    searchStr = ""
    requestAddStr = ""
    xiaoquDateAddCount = 30
    count = 0
    countquery = 0
    qqfobiden = 0
    for city in citys:
        countys = partOneObjs[city].keys()
        for county in countys:

            chose = whichCity(city, startExecuteBtn)
            if chose == False:
                continue

            areas = partOneObjs[city][county].keys()

            execWhichStep = "toutiao选城市取数据/1今日头条1定位到地方.txt"
            startExecuteBtn['text'] = execWhichStep
            t3 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t3.start()
            t3.join()
            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/1今日头条1定位到地方.txt"
            startExecuteBtn['text'] = execWhichStep
            t3 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t3.start()
            t3.join()
            time.sleep(20)

            execWhichStep = "toutiao选城市取数据/2进入选地方.txt"
            startExecuteBtn['text'] = execWhichStep
            # UIUpdateCutDownExecute(6, custom_thread_list).start()
            t21 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t21.start()
            t21.join()
            time.sleep(10)



            execWhichStep = "toutiao选城市取数据/2.1"+city+".txt"
            startExecuteBtn['text'] = execWhichStep
            t21 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t21.start()
            t21.join()

            time.sleep(20)
            execWhichStep = "toutiao选城市取数据/3.1选择进入抓包软件HttpCanary3.txt"
            startExecuteBtn['text'] = execWhichStep
            t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t31.start()
            t31.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/3.2选择第一项抓包列表.txt"
            startExecuteBtn['text'] = execWhichStep
            t32 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t32.start()
            t32.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/3.3进入请求结果.txt"
            startExecuteBtn['text'] = execWhichStep
            t33 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t33.start()
            t33.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/3.4点请求结果详情.txt"
            startExecuteBtn['text'] = execWhichStep
            t34 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t34.start()
            t34.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/3.5保存结果.txt"
            startExecuteBtn['text'] = execWhichStep
            t35 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t35.start()
            t35.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/3.6返回抓包主页.txt"
            startExecuteBtn['text'] = execWhichStep
            t36 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t36.start()
            t36.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/4.1选择进入文件管理软件4-已初始can-json-选好第一项.txt"
            startExecuteBtn['text'] = execWhichStep
            t41 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t41.start()
            t41.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/4.2点json文件夹.txt"
            startExecuteBtn['text'] = execWhichStep
            t42 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t42.start()
            t42.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/4.3不用勾选删除第一项.txt"
            startExecuteBtn['text'] = execWhichStep
            t43 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t43.start()
            t43.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/4.4勾选第一项发送dbbqbq.txt"
            startExecuteBtn['text'] = execWhichStep
            t44 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t44.start()
            t44.join()

            time.sleep(30)
            execWhichStep = "toutiao选城市取数据/4.4.1在qq2上选dbbqbq.txt"
            startExecuteBtn['text'] = execWhichStep
            t44 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t44.start()
            t44.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/4.5qq2软件上点发送文件按钮.txt"
            startExecuteBtn['text'] = execWhichStep
            t45 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t45.start()
            t45.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/5回到今日头条.txt"
            startExecuteBtn['text'] = execWhichStep
            t5 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t5.start()
            t5.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/6.1qq接收文件.txt"
            startExecuteBtn['text'] = execWhichStep
            t61 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t61.start()
            t61.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/6.2打开文件.txt"
            startExecuteBtn['text'] = execWhichStep
            t62 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t62.start()
            t62.join()

            time.sleep(10)
            execWhichStep = "toutiao选城市取数据/6.3全选内容并复制.txt"
            startExecuteBtn['text'] = execWhichStep
            t63 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
            t63.start()
            t63.join()

            msgStr = getClipboardText()

            print(msgStr)
            print("getmsg 完成")

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



                        #time.sleep(120)


    area1_xiaoqufile.close()


def whichCity(city,startExecuteBtn):
    chose=False
    if city == "中山":
        chose = True
    if city == "珠海":
        chose = True
    if city == "郑州":
        chose = True
    return chose

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





def searchMsg(city,county,area,xiaoquname):

    searchXiaoquName = ""
    xiaoqunameleftright = xiaoquname.split("·")
    if len(xiaoqunameleftright) > 1:
        searchXiaoquName = xiaoqunameleftright[1]
    else:
        searchXiaoquName = xiaoquname

    xiaoqumsg = {}
    xiaoqumsg[xiaoquname]=[]

    shouhumediasrc_dir = r'../../'  # 源文件目录地址
    files = list_all_files(shouhumediasrc_dir)
    for filepath in files:
        filename = os.path.basename(filepath)
        if filename.find("shouhumedia")!=-1 :
            print(filename)
            mediafile = open(filepath, 'r+', encoding='utf-8')
            filecontent = mediafile.read()
            mediaObjs= json.loads(filecontent)
            titles = mediaObjs.keys()
            for title in titles:
                if title.find(county)!=-1:
                    obj={}
                    obj["title"]=title
                    obj["url"]=mediaObjs[title]
                    obj["xiaoquname"] = xiaoquname
                    xiaoqumsg[xiaoquname].append(obj)
                if title.find(area) != -1:
                    obj = {}
                    obj["title"] = title
                    obj["url"] = mediaObjs[title]
                    obj["xiaoquname"] = xiaoquname
                    xiaoqumsg[xiaoquname].append(obj)
                if title.find(city) != -1:
                    obj = {}
                    obj["title"] = title
                    obj["url"] = mediaObjs[title]
                    obj["xiaoquname"] = xiaoquname
                    xiaoqumsg[xiaoquname].append(obj)
                if title.find(xiaoquname) != -1:
                    obj = {}
                    obj["title"] = title
                    obj["url"] = mediaObjs[title]
                    obj["xiaoquname"]=xiaoquname
                    xiaoqumsg[xiaoquname].append(obj)
            mediafile.close()

    return xiaoqumsg


