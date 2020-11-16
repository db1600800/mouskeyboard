import json
import threading
import time
import tkinter

import pyperclip
from addgroup_mycreategroup import *

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

    def __init__(self, file_name, execute_count):
        super().__init__()
        self.execute_count = execute_count
        self.file_name = file_name

    def run(self):

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
        qqcitypage1 = [{"qq": "1702478760", "city": ['衡水', '海南', '哈尔滨']},
                       {"qq": "3389252161", "city": ['惠州', '合肥', '防城港']}]
        qqcitypage2 = [{"qq": "3232475351", "city": ['泰州', '清远', '天津']},
                       {"qq": "1304789309", "city": ['临沂', '唐山', '太原']},
                       {"qq": "2786546813", "city": ['台州', '苏州', '石家庄']},
                       {"qq": "2841262285", "city": ['深圳', '沈阳', '绍兴']}
                       ]
        qqcitypage3 = [{"qq": "1217275070", "city": ['扬州', '淄博', '珠海']},
                       {"qq": "1659127292", "city": ['舟山', '威海', '中山']}]

        '''
        for oneqq in qqcitypage1:
            qqnum = oneqq["qq"]
            citys = oneqq["city"]
            city = citys[random.randint(0, len(citys) - 1)]
            qqAddGroup(startExecuteBtn, "area_page1", qqnum)
            qqAddGroup(startExecuteBtn, "area_page2", qqnum)
            qqAddGroup(startExecuteBtn, "area_page3", qqnum)

        for oneqq in qqcitypage2:
            qqnum = oneqq["qq"]
            citys = oneqq["city"]
            city = citys[random.randint(0, len(citys) - 1)]
            qqAddGroup(startExecuteBtn, "area_page1", qqnum)
            qqAddGroup(startExecuteBtn, "area_page2", qqnum)
            qqAddGroup(startExecuteBtn, "area_page3", qqnum)

        for oneqq in qqcitypage3:
            qqnum = oneqq["qq"]
            citys = oneqq["city"]
            city = citys[random.randint(0, len(citys) - 1)]
            qqAddGroup(startExecuteBtn, "area_page1", qqnum)
            qqAddGroup(startExecuteBtn, "area_page2", qqnum)
            qqAddGroup(startExecuteBtn, "area_page3", qqnum)
        '''

        for oneqq in qqcitypage1:
            qqnum = oneqq["qq"]
            citys = oneqq["city"]
            city = citys[random.randint(0, len(citys) - 1)]
            qqAddGroup2(startExecuteBtn, "area_page1", qqnum)
            qqAddGroup2(startExecuteBtn, "area_page2", qqnum)
            qqAddGroup2(startExecuteBtn, "area_page3", qqnum)

        for oneqq in qqcitypage2:
            qqnum = oneqq["qq"]
            citys = oneqq["city"]
            city = citys[random.randint(0, len(citys) - 1)]
            qqAddGroup2(startExecuteBtn, "area_page1", qqnum)
            qqAddGroup2(startExecuteBtn, "area_page2", qqnum)
            qqAddGroup2(startExecuteBtn, "area_page3", qqnum)

        for oneqq in qqcitypage3:
            qqnum = oneqq["qq"]
            citys = oneqq["city"]
            city = citys[random.randint(0, len(citys) - 1)]
            qqAddGroup2(startExecuteBtn, "area_page1", qqnum)
            qqAddGroup2(startExecuteBtn, "area_page2", qqnum)
            qqAddGroup2(startExecuteBtn, "area_page3", qqnum)



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




if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('按键精灵-加群')
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