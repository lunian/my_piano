# -*- coding: utf-8 -*-
#!C:\Users\lenovo\AppData\Local\Programs\Python\Python36-32\python.exe

import ctypes
import msvcrt
i = 0
while True:
    c = msvcrt.getche().decode("utf8","ignore")           # 输入一个字母，无需按回车键确认输入
    ctypes.windll.winmm.mciSendStringW("open sound\\%s.mp3 alias s%d" % (c,i) , None, 0, None)
    ctypes.windll.winmm.mciSendStringW("play s%d" % i, None, 0, None)
    i += 1
