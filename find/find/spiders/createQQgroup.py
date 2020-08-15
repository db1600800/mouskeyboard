import json
import random
import os
import re
from qqkeyboard_createqqgroup import *

def qqAddGroup(startExecuteBtn):
    global execWhichStep
    whichpage="area_page3"
    area1_xiaoqufile = open(whichpage+"_creategroup.json", 'r+', encoding='utf-8')
    filecontent = area1_xiaoqufile.read()
    area1_xiaoqufile.close()
    partOneObjs = json.loads(filecontent)
    citys = partOneObjs.keys()
    # citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']
    #dict_keys(['扬州', '淄博', '珠海', '舟山', '威海', '中山', '郑州', '镇江', '漳州', '湛江', '岳阳', '银川', '徐州', '烟台', '厦门', '西宁', '西安', '武汉', '芜湖', '无锡', '温州', '潍坊'])
    #page3 中山 珠海 郑州 扬州 漳州 厦门 徐州
    #page1 惠州 佛山  长沙 合肥 重庆 福州 东莞      贵阳
    #page2 天津 清远 台州 泉州 深圳 石家庄 宁波 三亚 南通 绍兴

    # page1-citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']
    # page2-citys=(['泰州', '清远', '天津', '临沂', '唐山', '太原', '台州', '苏州', '石家庄', '沈阳', '深圳', '绍兴', '上海', '三亚', '泉州', '庆阳', '青岛', '宁波', '南通', '南宁', '南京', '南充', '南昌', '吉林', '洛阳', '泸州', '连云港', '廊坊', '乐山', '兰州', '昆山', '昆明', '九江', '江门', '金华', '嘉兴', '济南', '济宁'])
    # page3_keys(['扬州', '淄博', '珠海', '舟山', '威海', '中山', '郑州', '镇江', '漳州', '湛江', '岳阳', '银川', '徐州', '烟台', '厦门', '西宁', '西安', '武汉', '芜湖', '无锡', '温州', '潍坊'])

    #citys = ['扬州']
    searchStr = ""
    requestAddStr = ""
    xiaoquDateAddCount = 2
    count = 0
    totalcount=0
    countquery = 0
    qqfobiden = 0
    for city in citys:
        countys = partOneObjs[city].keys()
        for county in countys:
            areas = partOneObjs[city][county].keys()
            for area in areas:
                xiaoqus = partOneObjs[city][county][area].keys()
                for xiaoqu in xiaoqus:

                    if qqfobiden == 6:
                        print("qqfobiden....")
                        return city, county, area, xiaoqu
                    if totalcount >= 8:
                        print("8 out....")
                        return city, county, area, xiaoqu
                    xiaoqudict = partOneObjs[city][county][area][xiaoqu]
                    if xiaoqudict.get("isRequestQQGroup") == None or  xiaoqudict["isRequestQQGroup"] == False:
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


                        searchStr= getCountyxiaoquname(county,xiaoquname)

                        execWhichStep = "建立群脚本/1点加号选加群.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t2.start()
                        t2.join()

                        execWhichStep = "建立群脚本/1.1隐藏列表.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t2 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t2.start()
                        t2.join()

                        time.sleep(2)
                        execWhichStep = "建立群脚本/2置业安家.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t2 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t2.start()
                        t2.join()


                        time.sleep(2)
                        setClipboardText(searchStr)
                        execWhichStep = "建立群脚本/3.1小区信息填写.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t3 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t3.start()
                        t3.join()
                        time.sleep(2)

                        setClipboardText(searchStr)
                        execWhichStep = "建立群脚本/3.2群信息填写并且下一步完成确定.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(6, custom_thread_list).start()
                        t21 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t21.start()
                        t21.join()
                        time.sleep(5)

                        execWhichStep = "建立群脚本/4恢复列表.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1,file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(2)

                        execWhichStep = "建立群脚本/5选择群右键修改群属性隐藏列表.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(2)

                        execWhichStep = "建立群脚本/6添加头像.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(1)

                        execWhichStep = "建立群脚本/7点编辑.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(1)

                        keystr=xiaoquname
                        setClipboardText(getEight(keystr))
                        execWhichStep = "建立群脚本/8设置关键词.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(5)

                        keystr = xiaoquname
                        listkeystr = list(keystr)
                        count = 1
                        eightstr = ""
                        for s in listkeystr:
                            if count <= 6 and count < len(listkeystr):
                                eightstr += s
                            count += 1
                        setClipboardText(eightstr+"业主")
                        execWhichStep = "建立群脚本/8设置关键词.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(5)


                        keystr = getCountyxiaoquname(area,xiaoquname)
                        setClipboardText(getEight(keystr))
                        execWhichStep = "建立群脚本/8设置关键词.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(5)


                        keystr = getCountyxiaoquname(county,xiaoquname)
                        setClipboardText(getEight(keystr))
                        execWhichStep = "建立群脚本/8设置关键词.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(2)


                        keystr = getCountyxiaoquname(city,xiaoquname)
                        setClipboardText(getEight(keystr))
                        execWhichStep = "建立群脚本/8设置关键词.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(5)

                        detail=xiaoquname+"业主交流群，进群请修改群名片，楼栋+昵称，物业、楼盘、购房置业、生活日常，大家畅所欲言，携手共建和谐社区"
                        setClipboardText(detail)
                        execWhichStep = "建立群脚本/9设置群介绍并按确定.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(2)

                        execWhichStep = "建立群脚本/10关闭编辑.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(5)

                        execWhichStep = "建立群脚本/11恢复列表.txt"
                        startExecuteBtn['text'] = execWhichStep
                        # UIUpdateCutDownExecute(1, custom_thread_list).start()
                        t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                        t31.start()
                        t31.join()
                        time.sleep(1)


                        xiaoqudict["isRequestQQGroup"] = True
                        area1_xiaoqufile_up = open(whichpage+"_creategroup.json", 'w+', encoding='utf-8')
                        area1_xiaoqufile_up.write(json.dumps(partOneObjs) + "\n")
                        area1_xiaoqufile_up.flush()
                        area1_xiaoqufile_up.close()
                        startExecuteBtn['state'] = 'normal'
                        print(city+county+area+xiaoquname+"    ctreate group点完成")
                        count += 1
                        totalcount+=1
                        print(" create group sucess: " + str(count) + " total:" + str(count + countquery))
                        time.sleep(120)
    print(city+"城市完成")




def getCountyxiaoquname(county,xiaoquname):
    countystr = county
    if county.find("市") != -1:
        countystr = county.replace("市", "")
    if county.find("区") != -1:
        countystr = county.replace("区", "")
    countyxiaoquname = ""
    if xiaoquname.find(countystr) != -1:
        countyxiaoquname = xiaoquname + ""
    else:
        countyxiaoquname = countystr + xiaoquname + ""
    return countyxiaoquname

def getEight(keystr):
    listkeystr = list(keystr)
    count = 1
    eightstr = ""
    for s in listkeystr:
        if count <= 8 and count < len(listkeystr):
            eightstr += s
        count += 1
    return  eightstr