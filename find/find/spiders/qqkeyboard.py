import json
import threading
import time
import tkinter
import random
import re
import os
import pyperclip

from pynput import keyboard, mouse
from pynput.keyboard import Controller as KeyBoardController, KeyCode
from pynput.mouse import Button, Controller as MouseController

global ismouselisten
ismouselisten=True

global execWhichStep
execWhichStep=""

# 键盘动作模板
def keyboard_action_template():
    return {
        "name": "keyboard",
        "event": "default",
        "target": "default",
        "action": "default",
        "location": {
            "x": "0",
            "y": "0"
        },
        "vk": "default",
        "time":0
    }


# 鼠标动作模板
def mouse_action_template():
    return {
        "name": "mouse",
        "event": "default",
        "target": "default",
        "action": "default",
        "location": {
            "x": "0",
            "y": "0"
        },
        "vk": "default",
        "time":0
    }


def getClipboardText():
    return pyperclip.paste()


def setClipboardText(aString):
    pyperclip.copy(aString)


# 倒计时监听，更新UI触发自定义线程对象
class UIUpdateCutDownExecute(threading.Thread):
    def __init__(self, cut_down_time, custom_thread_list):
        super().__init__()
        self.cut_down_time = cut_down_time
        self.custom_thread_list = custom_thread_list

    def run(self):
        while self.cut_down_time > 0:
            for custom_thread in self.custom_thread_list:
                if custom_thread['obj_ui'] is not None:
                    button=custom_thread['obj_ui']
                    custom_thread['obj_ui']['text'] = str(self.cut_down_time)
                    custom_thread['obj_ui']['state'] = 'disabled'
                    self.cut_down_time = self.cut_down_time - 1
            time.sleep(1)
        else:
            for custom_thread in self.custom_thread_list:
                if custom_thread['obj_ui'] is not None:
                    custom_thread['obj_ui']['text'] = custom_thread['final_text']
                    custom_thread['obj_ui']['state'] = 'disabled'
                if custom_thread['obj_thread'] is not None:
                    custom_thread['obj_thread'].start()
                    time.sleep(1)


# 键盘动作监听
class KeyboardActionListener(threading.Thread):

    def __init__(self, file_name='keyboard.action'):
        super().__init__()
        self.file_name = file_name

    def run(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            # 键盘按下监听
            def on_press(key):
                template = keyboard_action_template()
                template['event'] = 'press'
                template['time'] = time.time()
                try:
                    template['vk'] = key.vk
                except AttributeError:
                    template['vk'] = key.value.vk
                finally:
                    file.writelines(json.dumps(template) + "\n")
                    file.flush()


            # 键盘抬起监听
            def on_release(key):
                if key == keyboard.Key.esc:
                    # 停止监听
                    startListenerBtn['text'] = '开始录制'
                    startListenerBtn['state'] = 'normal'
                    keyboardListener.stop()
                    global ismouselisten
                    ismouselisten =False
                    conbin()
                    return False
                template = keyboard_action_template()
                template['event'] = 'release'
                template['time'] = time.time()
                try:
                    template['vk'] = key.vk
                except AttributeError:
                    template['vk'] = key.value.vk
                finally:
                    file.writelines(json.dumps(template) + "\n")
                    file.flush()


            # 键盘监听
            with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboardListener:
                keyboardListener.join()


# 键盘动作执行
"""
class KeyboardActionExecute(threading.Thread):

    def __init__(self, file_name='keyboard.action', execute_count=0):
        super().__init__()
        self.file_name = file_name
        self.execute_count = execute_count

    def run(self):
        while self.execute_count > 0:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                keyboard_exec = KeyBoardController()
                line = file.readline()
                while line:
                    obj = json.loads(line)
                    if obj['name'] == 'keyboard':
                        if obj['event'] == 'press':
                            keyboard_exec.press(KeyCode.from_vk(obj['vk']))
                            time.sleep(0.01)

                        elif obj['event'] == 'release':
                            keyboard_exec.release(KeyCode.from_vk(obj['vk']))
                            time.sleep(0.01)
                    line = file.readline()
                startExecuteBtn['text'] = '开始回放'
                startExecuteBtn['state'] = 'normal'
            self.execute_count = self.execute_count - 1
"""

# 鼠标动作监听
class MouseActionListener(threading.Thread):

    def __init__(self, file_name='mouse.action'):
        super().__init__()
        self.file_name = file_name

    def run(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            # 鼠标移动事件
            def on_move(x, y):
                template = mouse_action_template()
                template['event'] = 'move'
                template['location']['x'] = x
                template['location']['y'] = y
                template['time'] = time.time()
                file.writelines(json.dumps(template) + "\n")
                file.flush()
                return ismouselisten

            # 鼠标点击事件
            def on_click(x, y, button, pressed):
                template = mouse_action_template()
                template['event'] = 'click'
                template['target'] = button.name
                template['action'] = pressed
                template['location']['x'] = x
                template['location']['y'] = y
                template['time'] = time.time()
                file.writelines(json.dumps(template) + "\n")
                file.flush()
                return ismouselisten

            # 鼠标滚动事件
            def on_scroll(x, y, x_axis, y_axis):
                template = mouse_action_template()
                template['event'] = 'scroll'
                template['location']['x'] = x_axis
                template['location']['y'] = y_axis
                template['time'] = time.time()
                file.writelines(json.dumps(template) + "\n")
                file.flush()
                return ismouselisten

            with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouseListener:
                mouseListener.join()


# 鼠标动作执行
class MouseActionExecute(threading.Thread):

    def __init__(self, file_name='mousekeyboard.action', execute_count=1):
        super().__init__()
        self.execute_count = execute_count

    def run(self):
        self.file_name = execWhichStep
        while self.execute_count > 0:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                mouse_exec = MouseController()
                keyboard_exec = KeyBoardController()
                line = file.readline()
                while line:
                    obj = json.loads(line)
                    if obj['name'] == 'keyboard':
                        if obj['event'] == 'press':
                            keyboard_exec.press(KeyCode.from_vk(obj['vk']))
                            time.sleep(0.01)
                        elif obj['event'] == 'release':
                            keyboard_exec.release(KeyCode.from_vk(obj['vk']))
                            time.sleep(0.01)
                    elif obj['name'] == 'mouse':
                        if obj['event'] == 'move':
                            mouse_exec.position = (obj['location']['x'], obj['location']['y'])
                            time.sleep(0.01)
                        elif obj['event'] == 'click':
                            if obj['action']:
                                if obj['target'] == 'left':
                                    mouse_exec.press(Button.left)
                                else:
                                    mouse_exec.press(Button.right)
                            else:
                                if obj['target'] == 'left':
                                    mouse_exec.release(Button.left)
                                else:
                                    mouse_exec.release(Button.right)
                            time.sleep(0.01)
                        elif obj['event'] == 'scroll':
                            mouse_exec.scroll(obj['location']['x'], obj['location']['y'])
                            time.sleep(0.01)
                    line = file.readline()
                #startExecuteBtn['text'] = '开始回放'
                #startExecuteBtn['state'] = 'normal'
            self.execute_count = self.execute_count - 1


def command_adapter(action):
    if action == 'listener':
        if startListenerBtn['text'] == '开始录制':
            custom_thread_list = [
                {
                    'obj_thread': KeyboardActionListener(),
                    'obj_ui': startListenerBtn,
                    'final_text': '录制中...esc停止录制'
                },
                {
                    'obj_thread': MouseActionListener(),
                    'obj_ui': None,
                    'final_text': None
                }
            ]
            global ismouselisten
            ismouselisten = True
            UIUpdateCutDownExecute(startTime.get(), custom_thread_list).start()

    elif action == 'execute':
        qqAddGroup()



def isNumber(content):
    if content.isdigit() or content == "":
        return True
    else:
        return False



global mousekeyboardlist
def conbin():
    mousekeyboardlist = []
    mousefile=open("mouse.action", 'r', encoding='utf-8')
    for mousefileline in mousefile.readlines():
         obj = json.loads(mousefileline)
         mousekeyboardlist.append(obj)
    mousefile.close()

    keyboardfile=open("keyboard.action", 'r', encoding='utf-8')
    for  keyboardfileline in keyboardfile.readlines():
            obj = json.loads(keyboardfileline)
            mousekeyboardlist.append(obj)
    keyboardfile.close()

    mousekeyboardlist.sort(key=lambda k: (k.get('time', 0)))

    mousekeyboradfile=open("mousekeyboard.action", 'w', encoding='utf-8')
    for item in mousekeyboardlist:
            mousekeyboradfile.writelines(json.dumps(item) + "\n")
            mousekeyboradfile.flush()
    mousekeyboradfile.close()


def qqAddGroup():
     global  execWhichStep
     area1_xiaoqufile = open("area_page1.json", 'r+', encoding='utf-8')
     filecontent = area1_xiaoqufile.read()
     partOneObjs = json.loads(filecontent)
     citys = partOneObjs.keys()
        # citys=['惠州', '北京', '防城港', '呼和浩特', '衡水', '合肥', '杭州', '海南', '哈尔滨', '桂林', '贵阳', '佛山', '福州', '东莞', '大连', '重庆', '长沙','长春', '成都', '常州', '包头', '保定']

     searchStr=""
     requestAddStr=""
     xiaoquDateAddCount=30
     count = 0
     countquery = 0
     qqfobiden=0
     for city in citys:
          countys=partOneObjs[city].keys()
          for county in countys:
             areas=partOneObjs[city][county].keys()
             for area in areas:
                xiaoqus=partOneObjs[city][county][area].keys()
                for xiaoqu in xiaoqus:

                    if count+countquery>xiaoquDateAddCount :
                        print("30out   ok: " + str(count) +"error:"+str(countquery)+ " total:" + str(count + countquery))
                        break
                    if qqfobiden==4:
                        print("qqfobiden....")
                        break

                    xiaoqudict=partOneObjs[city][county][area][xiaoqu]
                    if xiaoqudict.get("isRequestQQGroup")==None :
                            xiaoquname=xiaoqudict["xiaoquname"]
                            href = xiaoqudict["href"]
                            address = xiaoqudict["address"]
                            dong = xiaoqudict["dong"]
                            fengqi = xiaoqudict["fengqi"]

                            dongs=dong.split('#,')
                            if dongs==[]:
                               dongs = dong.split('...,')
                            if dongs == []:
                               dongs = dong.split('号楼,')
                            if dongs == []:
                               dongs = dong.split('#楼,')
                            dongStr=""
                            if dongs==None or dongs==[]:
                                dongStr = "业主"
                            else:
                                dongcount=len(dongs)
                                d=""
                                if dongcount>2:
                                  d=dongs[dongcount-1]
                                  if d=="":
                                       d=dongs[dongcount-2]
                                else:
                                  d = dongs[dongcount - 1]
                                r=random.randrange(4,7,1)
                                dongStr=d+"栋"+str(r)+"01"
                            requestAddStr=xiaoquname+dongStr
                            searchStr=city+" "+xiaoquname

                            if countquery==0 and count==0:
                                execWhichStep="加群脚本/1.qq加群窗口定位.txt"
                                startExecuteBtn['text'] = execWhichStep
                                startExecuteBtn['state'] = 'disabled'
                                custom_thread_list = [{'obj_thread': MouseActionExecute(execute_count=playCount.get()),'obj_ui': startExecuteBtn,'final_text': '回放中...关闭程序停止回放'}]
                                #UIUpdateCutDownExecute(1, custom_thread_list).start()
                                t1=MouseActionExecute(execute_count=playCount.get())
                                t1.start()
                                t1.join()



                            execWhichStep = "加群脚本/2.按下输入框清除按钮.txt"
                            startExecuteBtn['text'] = execWhichStep
                            #UIUpdateCutDownExecute(6, custom_thread_list).start()
                            t2 = MouseActionExecute(execute_count=playCount.get())
                            t2.start()
                            t2.join()



                            setClipboardText(searchStr)
                            execWhichStep = "加群脚本/3.输入口粘贴小区名并按搜索.txt"
                            startExecuteBtn['text'] = execWhichStep
                            #UIUpdateCutDownExecute(6, custom_thread_list).start()
                            t3 = MouseActionExecute(execute_count=playCount.get())
                            t3.start()
                            t3.join()

                            time.sleep(6)
                            execWhichStep = "加群脚本/3.1搜索结果单元1信息拷贝.txt"
                            startExecuteBtn['text'] = execWhichStep
                            #UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t31 = MouseActionExecute(execute_count=playCount.get())
                            t31.start()
                            t31.join()
                            cell1Str = getClipboardText()
                            print(cell1Str)
                            if cell1Str==None or cell1Str=="":
                                 qqfobiden+=1

                            time.sleep(1)
                            execWhichStep = "加群脚本/3.2搜索结果单元2信息拷贝.txt"
                            startExecuteBtn['text'] = execWhichStep
                            #UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t32 = MouseActionExecute(execute_count=playCount.get())
                            t32.start()
                            t32.join()
                            cell2Str = getClipboardText()
                            print(cell2Str)

                            time.sleep(1)
                            execWhichStep = "加群脚本/3.3搜索结果单元3信息拷贝.txt"
                            startExecuteBtn['text'] = execWhichStep
                            #UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t33 = MouseActionExecute(execute_count=playCount.get())
                            t33.start()
                            t33.join()
                            cell3Str = getClipboardText()
                            print(cell3Str)

                            time.sleep(1)
                            execWhichStep = "加群脚本/3.4搜索结果单元4信息拷贝.txt"
                            startExecuteBtn['text'] = execWhichStep
                            #UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t34 = MouseActionExecute(execute_count=playCount.get())
                            t34.start()
                            t34.join()
                            cell4Str = getClipboardText()
                            print(cell4Str)

                            time.sleep(1)
                            execWhichStep = "加群脚本/3.5搜索结果单元5信息拷贝.txt"
                            startExecuteBtn['text'] = execWhichStep
                            #UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t35 = MouseActionExecute(execute_count=playCount.get())
                            t35.start()
                            t35.join()
                            cell5Str = getClipboardText()
                            print(cell5Str)

                            time.sleep(1)
                            execWhichStep = "加群脚本/3.6搜索结果单元6信息拷贝.txt"
                            startExecuteBtn['text'] = execWhichStep
                            # UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t36 = MouseActionExecute(execute_count=playCount.get())
                            t36.start()
                            t36.join()
                            cell6Str = getClipboardText()
                            print(cell6Str)


                            if checkCellWhichOk(cell1Str,xiaoquname)==True:
                                print("query  find 4.1" + str(countquery))
                                execWhichStep = "加群脚本/4.1点单元1加群按钮.txt"
                                startExecuteBtn['text'] = execWhichStep
                                #UIUpdateCutDownExecute(1, custom_thread_list).start()
                                t41 = MouseActionExecute(execute_count=playCount.get())
                                t41.start()
                                t41.join()
                            elif checkCellWhichOk(cell2Str,xiaoquname) == True:
                                print("query  find 4.2" + str(countquery))
                                execWhichStep = "加群脚本/4.2点单元2加群按钮.txt"
                                startExecuteBtn['text'] = execWhichStep
                                #UIUpdateCutDownExecute(1, custom_thread_list).start()
                                t42 = MouseActionExecute(execute_count=playCount.get())
                                t42.start()
                                t42.join()
                            elif checkCellWhichOk(cell3Str,xiaoquname) == True:
                                print("query  find 4.3" + str(countquery))
                                execWhichStep = "加群脚本/4.3点单元3加群按钮.txt"
                                startExecuteBtn['text'] = execWhichStep
                                #UIUpdateCutDownExecute(1, custom_thread_list).start()
                                t43 = MouseActionExecute(execute_count=playCount.get())
                                t43.start()
                                t43.join()
                            elif checkCellWhichOk(cell4Str,xiaoquname) == True:
                                print("query  find 4.4" + str(countquery))
                                execWhichStep = "加群脚本/4.4点单元4加群按钮.txt"
                                startExecuteBtn['text'] = execWhichStep
                                #UIUpdateCutDownExecute(1, custom_thread_list).start()
                                t44 = MouseActionExecute(execute_count=playCount.get())
                                t44.start()
                                t44.join()
                            elif checkCellWhichOk(cell5Str,xiaoquname) == True:
                                print("query  find 4.5" + str(countquery))
                                execWhichStep = "加群脚本/4.5点单元5加群按钮.txt"
                                startExecuteBtn['text'] = execWhichStep
                                #UIUpdateCutDownExecute(1, custom_thread_list).start()
                                t45 = MouseActionExecute(execute_count=playCount.get())
                                t45.start()
                                t45.join()
                            elif checkCellWhichOk(cell6Str,xiaoquname) == True:
                                print("query  find 4.6" + str(countquery))
                                execWhichStep = "加群脚本/4.6点单元6加群按钮.txt"
                                startExecuteBtn['text'] = execWhichStep
                                #UIUpdateCutDownExecute(1, custom_thread_list).start()
                                t46 = MouseActionExecute(execute_count=playCount.get())
                                t46.start()
                                t46.join()
                            else:
                                countquery += 1
                                print("query no find "+str(countquery)+" sucess:"+str(count))
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
                            print("query  find 5.粘贴加群信息并下一步  "+requestAddStr)
                            startExecuteBtn['text'] = execWhichStep
                            #UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t5 = MouseActionExecute(execute_count=playCount.get())
                            t5.start()
                            t5.join()

                            time.sleep(6)
                            execWhichStep = "加群脚本/6.点完成.txt"
                            startExecuteBtn['text'] = execWhichStep
                            #UIUpdateCutDownExecute(1, custom_thread_list).start()
                            t6 = MouseActionExecute(execute_count=playCount.get())
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
                            count+=1
                            print("add group sucess: " +str(count)+" total:"+ str(count+countquery))

     area1_xiaoqufile.close()

def checkCellWhichOk(cellStr,xiaoquname):

    cellStrleft = cellStr.split("/")
    if cellStrleft==None or cellStrleft==[]:
        return False
    if cellStr.find("品牌.产品")!=-1:
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


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('按键精灵-蓝士钦')
    root.geometry('200x200+400+100')

    listenerStartLabel = tkinter.Label(root, text='录制倒计时')
    listenerStartLabel.place(x=10, y=10, width=80, height=20)
    startTime = tkinter.IntVar()
    listenerStartEdit = tkinter.Entry(root, textvariable=startTime)
    listenerStartEdit.place(x=100, y=10, width=60, height=20)
    startTime.set(3)

    listenerTipLabel = tkinter.Label(root, text='秒')
    listenerTipLabel.place(x=160, y=10, width=20, height=20)

    startListenerBtn = tkinter.Button(root, text="开始录制", command=lambda: command_adapter('listener'))
    startListenerBtn.place(x=10, y=45, width=180, height=30)

    executeEndLabel = tkinter.Label(root, text='回放倒计时')
    executeEndLabel.place(x=10, y=85, width=80, height=20)
    endTime = tkinter.IntVar()
    executeEndEdit = tkinter.Entry(root, textvariable=endTime)
    executeEndEdit.place(x=100, y=85, width=60, height=20)
    endTime.set(6)

    executeTipLabel = tkinter.Label(root, text='秒')
    executeTipLabel.place(x=160, y=85, width=20, height=20)

    playCountLabel = tkinter.Label(root, text='回放次数')
    playCountLabel.place(x=10, y=115, width=80, height=20)
    playCount = tkinter.IntVar()
    playCountEdit = tkinter.Entry(root, textvariable=playCount)
    playCountEdit.place(x=100, y=115, width=60, height=20)
    playCount.set(1)

    playCountTipLabel = tkinter.Label(root, text='次')
    playCountTipLabel.place(x=160, y=115, width=20, height=20)

    startExecuteBtn = tkinter.Button(root, text="开始回放", command=lambda: command_adapter('execute'))
    startExecuteBtn.place(x=10, y=145, width=180, height=30)
    root.mainloop()