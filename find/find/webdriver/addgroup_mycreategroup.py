import json
import random
import os
import re
from qqkeyboard_addgroup_mycreategroup import *

def qqAddGroup(startExecuteBtn,whichpagep,qqnum):
    global execWhichStep
    whichpage=whichpagep
    area1_xiaoqufile = open(whichpage+"_creategroup.json", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    partOneObjs = json.loads(filecontent)
    area1_xiaoqufile.close()
    citys = partOneObjs.keys()
    # citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']
    #dict_keys(['扬州', '淄博', '珠海', '舟山', '威海', '中山', '郑州', '镇江', '漳州', '湛江', '岳阳', '银川', '徐州', '烟台', '厦门', '西宁', '西安', '武汉', '芜湖', '无锡', '温州', '潍坊'])
    #page3 中山 珠海 郑州 扬州 漳州 厦门 徐州
    #page1 惠州 佛山  长沙 合肥 重庆 福州 东莞      贵阳
    #page2 天津 清远 台州 泉州 深圳 石家庄 宁波 三亚 南通 绍兴

    #citys = ['武汉']

    execWhichStep = "切换Q/0恢复列表.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()
    time.sleep(2)

    execWhichStep = "切换Q/1切换帐号.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()

    time.sleep(20)
    setClipboardText(qqnum)
    execWhichStep = "切换Q/2粘贴号码.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()

    time.sleep(2)
    execWhichStep = "切换Q/4登陆.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()

    time.sleep(15)
    execWhichStep = "切换Q/5.1打开加群界面并隐藏列表.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()

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

                        print("30out   ok: " + str(count) + "error:" + str(countquery) + " total:" + str(
                            count + countquery))
                        #return city, county, area, xiaoqu
                        count=0
                        countquery=0
                        print("sleep 10 min")
                        time.sleep(300)
                    if qqfobiden == 6:
                        print("qqfobiden....")
                        return city, county, area, xiaoqu

                    xiaoqudict = partOneObjs[city][county][area][xiaoqu]
                    if xiaoqudict.get("qqnum") != None and xiaoqudict.get("qqnum") != qqnum and  xiaoqudict.get("groupnum")!=None :

                        xiaoquname = xiaoqudict["xiaoquname"]
                        href = xiaoqudict["href"]
                        address = xiaoqudict["address"]
                        if xiaoqudict.get("dong")==None:
                            continue
                        dong = xiaoqudict["dong"]
                        fengqi = xiaoqudict["fengqi"]

                        dongs = dong.split('#,')
                        if dongs == [] or dongs[0]==dong:
                            dongs = dong.split('...,')
                        if dongs == [] or dongs[0]==dong:
                            dongs = dong.split('号楼,')
                        if dongs == [] or dongs[0]==dong:
                            dongs = dong.split('#楼,')
                        dongStr = ""
                        if dongs == None or dongs == [] or dongs[0]==dong:
                            dongStr = "业主"
                        else:
                            dongcount = len(dongs)
                            d = ""
                            if dongcount > 2:
                                d = dongs[dongcount - 2]
                                if d == "":
                                    d = dongs[dongcount - 3]
                            else:
                                d = dongs[dongcount - 2]
                            r = random.randrange(4, 7, 1)
                            if d == "":
                                d = "1"
                            if d=="...,":
                                d="1"
                            dongStr = d + "栋" + str(r) + "01"
                        requestAddStr = xiaoquname + dongStr

                        searchStr =xiaoqudict["groupnum"]
                        time.sleep(10)
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

                        time.sleep(3)
                        execWhichStep = "加群脚本/2.按下输入框清除按钮.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t2 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t2.start()
                        t2.join()
                        time.sleep(3)
                        setClipboardText(searchStr)
                        execWhichStep = "加群脚本/3.输入口粘贴小区名并按搜索.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t3 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t3.start()
                        t3.join()

                        time.sleep(6)

                        execWhichStep = "加群脚本/2.1网络提示关闭.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t21 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t21.start()
                        t21.join()
                        time.sleep(1)

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



                        if checkCellWhichOk(cell1Str, xiaoquname) == True:
                            print("query  find 4.1" + str(countquery))
                            execWhichStep = "加群脚本/4.1点单元1加群按钮.txt"
                            startExecuteBtn['text'] = execWhichStep
                            # UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t41 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                            t41.start()
                            t41.join()
                        else:
                            countquery += 1
                            print(dong+" query no find " + str(countquery) + " sucess:" + str(count))
                            time.sleep(10)
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

                        time.sleep(60)
                        count += 1
                        print(" add group sucess: " + str(count) + " total:" + str(count + countquery))
    print("城市完成")


def qqAddGroup2(startExecuteBtn,qqnum,whichQQGroupWantMenber):
    if qqnum==whichQQGroupWantMenber:
        return


    # citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']
    #dict_keys(['扬州', '淄博', '珠海', '舟山', '威海', '中山', '郑州', '镇江', '漳州', '湛江', '岳阳', '银川', '徐州', '烟台', '厦门', '西宁', '西安', '武汉', '芜湖', '无锡', '温州', '潍坊'])
    #page3 中山 珠海 郑州 扬州 漳州 厦门 徐州
    #page1 惠州 佛山  长沙 合肥 重庆 福州 东莞      贵阳
    #page2 天津 清远 台州 泉州 深圳 石家庄 宁波 三亚 南通 绍兴

    #citys = ['武汉']

    execWhichStep = "切换Q/0恢复列表.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()
    time.sleep(2)

    execWhichStep = "切换Q/1切换帐号.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()

    time.sleep(20)
    setClipboardText(qqnum)
    execWhichStep = "切换Q/2粘贴号码.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()

    time.sleep(2)
    execWhichStep = "切换Q/4登陆.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()

    time.sleep(15)
    execWhichStep = "切换Q/5.1打开加群界面并隐藏列表.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t2.start()
    t2.join()

    searchStr = ""
    requestAddStr = "找组织"
    xiaoquDateAddCount = 30
    count = 0
    countquery = 0
    qqfobiden = 0



    time.sleep(10)
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

    time.sleep(3)
    execWhichStep = "加群脚本/2.按下输入框清除按钮.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t2 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
    t2.start()
    t2.join()
    time.sleep(3)
    setClipboardText(whichQQGroupWantMenber)
    execWhichStep = "加群脚本/3.输入口粘贴小区名并按搜索.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t3 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
    t3.start()
    t3.join()

    time.sleep(6)

    execWhichStep = "加群脚本/2.1网络提示关闭.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(6, custom_thread_list).start()
    t21 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
    t21.start()
    t21.join()
    time.sleep(1)

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




    print("query  find 4.1" + str(countquery))
    execWhichStep = "加群脚本/4.1点单元1加群按钮.txt"
    startExecuteBtn['text'] = execWhichStep
    # UIUpdateCutDownExecute(1, custom_thread_list).start()
    t41 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
    t41.start()
    t41.join()


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

    time.sleep(60)

    print(" add group sucess: " + str(count) + " total:" + str(count + countquery))




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



    if xiaoqunamematch==True and isnum==True and int(usercount)>0 and cellStr.find("置业安家")!=-1:
        return  True
    else:
        return False

