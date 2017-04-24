import numpy as np
from grabscreen import grab_screen
import time
from directkeys import PressKey,ReleaseKey, UP, DOWN
from getkeys import key_check
import random
import win32con

def main():

    print ("Checking for key-press...")
    paused = False
    while(True):

        time.sleep(0.09)
        
        keys = key_check()

        if win32con.VK_UP in keys:
            print ("UP")
        if win32con.VK_DOWN in keys:
            print ("DOWN")    

main()       
