# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi
import time
import win32con

keyList1 = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList1.append(char)

keyList2 = [win32con.VK_UP,win32con.VK_DOWN,win32con.VK_LEFT,win32con.VK_RIGHT]

def key_check():
    keys = []
    #for key in keyL:
    for key in keyList1:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    for key in keyList2:    
        if wapi.GetAsyncKeyState(key):
            keys.append(key)
    return keys
 
