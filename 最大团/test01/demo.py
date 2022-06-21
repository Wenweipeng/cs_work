
from ctypes import windll
from tkinter import *

app = Tk()

array_x = []
array_y = []

# 通过event形参来获取对应事件描述


def callback(event):
    print("当前位置：", event.x, event.y)
    # print(type(event.x))
    # print(type(int(event.x)))
    array_list(array_x, array_y, event.x, event.y)


def array_list(array_x, array_y, x, y):
    array_x.append(x)
    array_y.append(y)


# 创建框架，窗口尺寸
width = windll.user32.GetSystemMetrics(0)
height = windll.user32.GetSystemMetrics(1)
frame = Frame(app, width=width*0.5, height=height*0.5)
# frame.bind("<Motion>",callback)
# array = []
frame.bind("<Button-1>", callback)
# print(array)
# frame.bind("<Button-2>", callback)
# frame.bind("<Button-3>", callback)
frame.pack()
print(array_x, array_y)
# <Button-1>Button：表示鼠标的点击事件 “—”左边是事件本身，右边是事件描述
# 1：表示左键 2：中间键的滚轮点击 3：右键

mainloop()


# width = windll.user32.GetSystemMetrics(0)
# height = windll.user32.GetSystemMetrics(1)
# print(width, height)
