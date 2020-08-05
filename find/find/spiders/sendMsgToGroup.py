import json
import random
import os
import re
from qqkeyboard_sendmsg import *

def sendMsgToG(startExecuteBtn):
    global execWhichStep
    area1_xiaoqufile = open("area_page1.json", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    partOneObjs = json.loads(filecontent)
    citys = partOneObjs.keys()
    # citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']
    citys = ['佛山']
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

                        searchStr=""
                        xiaoqunameleftright = xiaoquname.split("·")
                        if len(xiaoqunameleftright) > 1:
                            searchStr=xiaoqunameleftright[1]
                        else:
                            searchStr = xiaoquname

                        msgStr=searchMsg(city,county,area,xiaoqu)


                        setClipboardText(searchStr)
                        execWhichStep = "向群发消息脚本/1选中搜索框并粘贴搜索"
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
                        time.sleep(120)


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


