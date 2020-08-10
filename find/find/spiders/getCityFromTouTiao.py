import json
import random
import os
import re
from qqkeyboard_city import *

def getMsgFromToutiao(startExecuteBtn):
            execWhichStep='{"name": "mouse", "event": "move", "target": "default", "action": "default","location": {"x": 481, "y":19 }, "vk": "default", "time": 1596762487.161921}'
            MouseActionExecuterun(execWhichStep)

            execWhichStep = '{"name": "mouse", "event": "click", "target": "left", "action": true, "location": {"x": 481, "y": 19},"vk": "default", "time": 1596769382.1209695}'
            MouseActionExecuterun(execWhichStep)

            execWhichStep = '{"name": "mouse", "event": "click", "target": "left", "action": false, "location": {"x": 481, "y": 19}, "vk": "default", "time": 1596769382.2489858}'
            MouseActionExecuterun(execWhichStep)
            time.sleep(1)

            y = 623

            time.sleep(1)



            while y<686:
                #列表右边滚动条向下一格
                str1=""
                setClipboardText("")
                execWhichStep = '{"name": "mouse", "event": "move", "target": "default", "action": "default","location": {"x": 707, "y":' + str(
                    y - 1) + ' }, "vk": "default", "time": 1596762487.161921}'
                MouseActionExecuterun(execWhichStep)
                str1+=execWhichStep

                execWhichStep = '{"name": "mouse", "event": "click", "target": "left", "action": true, "location": {"x": 707, "y": '+str(y-1)+'}, "vk": "default", "time": 1596762486.3298154}'
                MouseActionExecuterun(execWhichStep)
                str1 += "\n" + execWhichStep

                execWhichStep='{"name": "mouse", "event": "move", "target": "default", "action": "default","location": {"x": 707, "y": '+str(y)+'}, "vk": "default", "time": 1596762487.161921}'
                MouseActionExecuterun(execWhichStep)
                str1 += "\n" + execWhichStep

                execWhichStep = '{"name": "mouse", "event": "click", "target": "left", "action": false, "location": {"x": 707, "y": '+str(y-1)+'}, "vk": "default", "time": 1596762486.3298154}'
                MouseActionExecuterun(execWhichStep)
                str1 += "\n" + execWhichStep
                print(y)
                #移动到最后一项
                execWhichStep = '{"name": "mouse", "event": "move", "target": "default", "action": "default","location": {"x": 486, "y":652}, "vk": "default", "time": 1596762487.161921}'
                MouseActionExecuterun(execWhichStep)
                str1 += "\n" + execWhichStep
                #点击最后一项
                time.sleep(2)
                execWhichStep = '{"name": "mouse", "event": "click", "target": "left", "action": true, "location": {"x": 486, "y":652 }, "vk": "default", "time": 1596762486.3298154}'
                MouseActionExecuterun(execWhichStep)
                str1 += "\n" + execWhichStep
                execWhichStep = '{"name": "mouse", "event": "click", "target": "left", "action": false, "location": {"x": 486, "y":652}, "vk": "default", "time": 1596762486.3298154}'
                MouseActionExecuterun(execWhichStep)
                str1 += "\n" + execWhichStep
                time.sleep(10)
                
                execWhichStep = "toutiao选城市取数据/3.1选择进入抓包软件HttpCanary3.txt"
                startExecuteBtn['text'] = execWhichStep
                t31 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t31.start()
                t31.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/3.2选择第一项抓包列表.txt"
                startExecuteBtn['text'] = execWhichStep
                t32 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t32.start()
                t32.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/3.3进入请求结果.txt"
                startExecuteBtn['text'] = execWhichStep
                t33 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t33.start()
                t33.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/3.4点请求结果详情.txt"
                startExecuteBtn['text'] = execWhichStep
                t34 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t34.start()
                t34.join()

                time.sleep(3)
                execWhichStep = "toutiao选城市取数据/3.5保存结果.txt"
                startExecuteBtn['text'] = execWhichStep
                t35 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t35.start()
                t35.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/3.6返回抓包主页.txt"
                startExecuteBtn['text'] = execWhichStep
                t36 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t36.start()
                t36.join()

                time.sleep(4)
                execWhichStep = "toutiao选城市取数据/4.1选择进入文件管理软件4-已初始can-json-选好第一项.txt"
                startExecuteBtn['text'] = execWhichStep
                t41 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t41.start()
                t41.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/4.2点json文件夹.txt"
                startExecuteBtn['text'] = execWhichStep
                t42 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t42.start()
                t42.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/4.2.1点json文件夹.txt"
                startExecuteBtn['text'] = execWhichStep
                t42 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t42.start()
                t42.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/4.3不用勾选删除第一项.txt"
                startExecuteBtn['text'] = execWhichStep
                t43 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t43.start()
                t43.join()

                time.sleep(3)
                execWhichStep = "toutiao选城市取数据/4.4勾选第一项发送dbbqbq.txt"
                startExecuteBtn['text'] = execWhichStep
                t44 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t44.start()
                t44.join()

                time.sleep(6)
                execWhichStep = "toutiao选城市取数据/4.4.1在qq2上选dbbqbq.txt"
                startExecuteBtn['text'] = execWhichStep
                t44 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t44.start()
                t44.join()

                time.sleep(3)
                execWhichStep = "toutiao选城市取数据/4.5qq2软件上点发送文件按钮.txt"
                startExecuteBtn['text'] = execWhichStep
                t45 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t45.start()
                t45.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/5回到今日头条.txt"
                startExecuteBtn['text'] = execWhichStep
                t5 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t5.start()
                t5.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/6.1qq接收文件.txt"
                startExecuteBtn['text'] = execWhichStep
                t61 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t61.start()
                t61.join()

                time.sleep(2)
                execWhichStep = "toutiao选城市取数据/6.2打开文件.txt"
                startExecuteBtn['text'] = execWhichStep
                t62 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t62.start()
                t62.join()

                time.sleep(5)
                execWhichStep = "toutiao选城市取数据/6.3全选内容并复制.txt"
                startExecuteBtn['text'] = execWhichStep
                t63 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t63.start()
                t63.join()

                msgStr = getClipboardText()

                if msgStr!="" and msgStr!=None :
                    weather = json.loads(msgStr)
                    cityname=weather["data"]["weather"]["city_name"]
                    havefile = os.path.exists("2.1" + cityname + ".txt")
                    if havefile==False:
                        print(cityname)
                        fo = open("2.1"+cityname+".txt", "w+")  # 存入文件中。。。
                        fo.write(str1)
                        fo.write('\n')
                        fo.close()

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
                time.sleep(10)

                execWhichStep = "toutiao选城市取数据/2进入选地方.txt"
                startExecuteBtn['text'] = execWhichStep
                # UIUpdateCutDownExecute(6, custom_thread_list).start()
                t21 = MouseActionExecute(execute_count=1, file_name=execWhichStep)
                t21.start()
                t21.join()
                time.sleep(2)

                y+=1


def whichCity(city,startExecuteBtn):
    chose=False



    if city == "中山":
        chose = True
    """
    if city == "珠海":
        chose = True
    
    if city == "郑州":
        chose = True
    """
    return chose