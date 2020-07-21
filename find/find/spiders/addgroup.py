import json
import random
import os
import re
from qqkeyboard import *

def qqAddGroup(startExecuteBtn):
    global execWhichStep
    area1_xiaoqufile = open("area_page1.json", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    partOneObjs = json.loads(filecontent)
    citys = partOneObjs.keys()
    # citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']
    citys = ['长沙']
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

                    if count + countquery > xiaoquDateAddCount:
                        area1_xiaoqufile.close()
                        file1 = open("area_page1_1.json", "r+")
                        file2 = open("area_page1.json", "w+")
                        s = file1.read()
                        w = file2.write(s)
                        file1.close()
                        file2.close()
                        print("30out   ok: " + str(count) + "error:" + str(countquery) + " total:" + str(
                            count + countquery))
                        return city, county, area, xiaoqu
                        time.sleep(300)
                    if qqfobiden == 6:
                        print("qqfobiden....")
                        return city, county, area, xiaoqu

                    xiaoqudict = partOneObjs[city][county][area][xiaoqu]
                    if xiaoqudict.get("isRequestQQGroup") == None:
                        xiaoquname = xiaoqudict["xiaoquname"]
                        href = xiaoqudict["href"]
                        address = xiaoqudict["address"]
                        dong = xiaoqudict["dong"]
                        fengqi = xiaoqudict["fengqi"]

                        dongs = dong.split('#,')
                        if dongs == []:
                            dongs = dong.split('...,')
                        if dongs == []:
                            dongs = dong.split('号楼,')
                        if dongs == []:
                            dongs = dong.split('#楼,')
                        dongStr = ""
                        if dongs == None or dongs == []:
                            dongStr = "业主"
                        else:
                            dongcount = len(dongs)
                            d = ""
                            if dongcount > 2:
                                d = dongs[dongcount - 1]
                                if d == "":
                                    d = dongs[dongcount - 2]
                            else:
                                d = dongs[dongcount - 1]
                            r = random.randrange(4, 7, 1)
                            if d == "":
                                d = "1"
                            if d=="...,":
                                d="1"
                            dongStr = d + "栋" + str(r) + "01"
                        requestAddStr = xiaoquname + dongStr
                        searchStr = city + " " + xiaoquname + " 业"

                        if countquery == 0 and count == 0:
                            execWhichStep = "加群脚本/1.qq加群窗口定位.txt"
                            startExecuteBtn['text'] = execWhichStep
                            startExecuteBtn['state'] = 'disabled'
                            custom_thread_list = [{'obj_thread': MouseActionExecute(execute_count=1,file_name=execWhichStep),
                                                   'obj_ui': startExecuteBtn, 'final_text': '回放中...关闭程序停止回放'}]
                            # UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t1 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                            t1.start()
                            t1.join()

                        execWhichStep = "加群脚本/2.按下输入框清除按钮.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t2 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t2.start()
                        t2.join()

                        setClipboardText(searchStr)
                        execWhichStep = "加群脚本/3.输入口粘贴小区名并按搜索.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t3 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t3.start()
                        t3.join()

                        time.sleep(6)
                        execWhichStep = "加群脚本/3.1搜索结果单元1信息拷贝.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        cell1Str = getClipboardText()
                        print(cell1Str)
                        if cell1Str == searchStr:
                            qqfobiden += 1

                        time.sleep(1)
                        execWhichStep = "加群脚本/3.2搜索结果单元2信息拷贝.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t32 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t32.start()
                        t32.join()
                        cell2Str = getClipboardText()
                        print(cell2Str)

                        time.sleep(1)
                        execWhichStep = "加群脚本/3.3搜索结果单元3信息拷贝.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t33 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t33.start()
                        t33.join()
                        cell3Str = getClipboardText()
                        print(cell3Str)

                        time.sleep(1)
                        execWhichStep = "加群脚本/3.4搜索结果单元4信息拷贝.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t34 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t34.start()
                        t34.join()
                        cell4Str = getClipboardText()
                        print(cell4Str)

                        time.sleep(1)
                        execWhichStep = "加群脚本/3.5搜索结果单元5信息拷贝.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t35 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t35.start()
                        t35.join()
                        cell5Str = getClipboardText()
                        print(cell5Str)

                        time.sleep(1)
                        execWhichStep = "加群脚本/3.6搜索结果单元6信息拷贝.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t36 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t36.start()
                        t36.join()
                        cell6Str = getClipboardText()
                        print(cell6Str)

                        if checkCellWhichOk(cell1Str, xiaoquname) == True:
                            print("query  find 4.1" + str(countquery))
                            execWhichStep = "加群脚本/4.1点单元1加群按钮.txt"
                            startExecuteBtn['text'] = execWhichStep
                            # UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t41 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                            t41.start()
                            t41.join()
                        elif checkCellWhichOk(cell2Str, xiaoquname) == True:
                            print("query  find 4.2" + str(countquery))
                            execWhichStep = "加群脚本/4.2点单元2加群按钮.txt"
                            startExecuteBtn['text'] = execWhichStep
                            # UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t42 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                            t42.start()
                            t42.join()
                        elif checkCellWhichOk(cell3Str, xiaoquname) == True:
                            print("query  find 4.3" + str(countquery))
                            execWhichStep = "加群脚本/4.3点单元3加群按钮.txt"
                            startExecuteBtn['text'] = execWhichStep
                            # UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t43 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                            t43.start()
                            t43.join()
                        elif checkCellWhichOk(cell4Str, xiaoquname) == True:
                            print("query  find 4.4" + str(countquery))
                            execWhichStep = "加群脚本/4.4点单元4加群按钮.txt"
                            startExecuteBtn['text'] = execWhichStep
                            # UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t44 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                            t44.start()
                            t44.join()
                        elif checkCellWhichOk(cell5Str, xiaoquname) == True:
                            print("query  find 4.5" + str(countquery))
                            execWhichStep = "加群脚本/4.5点单元5加群按钮.txt"
                            startExecuteBtn['text'] = execWhichStep
                            # UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t45 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                            t45.start()
                            t45.join()
                        elif checkCellWhichOk(cell6Str, xiaoquname) == True:
                            print("query  find 4.6" + str(countquery))
                            execWhichStep = "加群脚本/4.6点单元6加群按钮.txt"
                            startExecuteBtn['text'] = execWhichStep
                            # UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t46 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                            t46.start()
                            t46.join()
                        else:
                            countquery += 1
                            print("query no find " + str(countquery) + " sucess:" + str(count))
                            xiaoqudict["isRequestQQGroup"] = False
                            area1_xiaoqufile_up = open("area_page1_1.json", 'w+', encoding='utf-8')
                            area1_xiaoqufile_up.write(json.dumps(partOneObjs) + "\n")
                            area1_xiaoqufile_up.flush()
                            area1_xiaoqufile_up.close()
                            time.sleep(120)
                            continue

                        time.sleep(6)

                        setClipboardText(requestAddStr)
                        execWhichStep = "加群脚本/5.粘贴加群信息并下一步.txt"
                        print("query  find 5.粘贴加群信息并下一步  " + requestAddStr)
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t5 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t5.start()
                        t5.join()

                        time.sleep(6)
                        execWhichStep = "加群脚本/6.点完成.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t6 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t6.start()
                        t6.join()
                        xiaoqudict["isRequestQQGroup"] = True
                        area1_xiaoqufile_up = open("area_page1_1.json", 'w+', encoding='utf-8')
                        area1_xiaoqufile_up.write(json.dumps(partOneObjs) + "\n")
                        area1_xiaoqufile_up.flush()
                        area1_xiaoqufile_up.close()
                        startExecuteBtn['state'] = 'normal'
                        print("query  find 6.点完成")
                        time.sleep(120)
                        count += 1
                        print("add group sucess: " + str(count) + " total:" + str(count + countquery))

    area1_xiaoqufile.close()


def checkCellWhichOk(cellStr,xiaoquname):

    cellStrleft = cellStr.split("/")
    if cellStrleft==None or cellStrleft==[]:
        return False
    if cellStr.find("品牌.产品")!=-1:
        return  False
    if cellStr.find("投资")!=-1:
        return  False
    usercount = re.sub("\D", "", cellStrleft[0])
    isnum=usercount.isdigit()

    xiaoqunamematch = False
    xiaoqunameleftright = xiaoquname.split("·")
    if len(xiaoqunameleftright) > 1:
        if cellStr.find(xiaoqunameleftright[1]) != -1:
            xiaoqunamematch = True
    else:
        if cellStr.find(xiaoquname) != -1:
            xiaoqunamematch = True


    haveyezhu=False
    if cellStr.find("业主") != -1:
        haveyezhu=True
    if xiaoqunamematch==True and isnum==True and int(usercount)>50 and haveyezhu==True:
        return  True
    else:
        return False

