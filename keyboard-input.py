# test_model.py

import numpy as np
from grabscreen import grab_screen
import time
from directkeys import PressKey,ReleaseKey, UP, DOWN
from getkeys import key_check
import random
import win32con

t_time = 0.09

def up():
    PressKey(UP)
    #ReleaseKey(DOWN)
    #time.sleep(t_time)
    #ReleaseKey(UP)
    
def down():
    PressKey(DOWN)
    #ReleaseKey(UP)
    #time.sleep(t_time)
    #ReleaseKey(DOWN)

def release():
    ReleaseKey(DOWN)
    ReleaseKey(UP)

def main():

    """
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    """        

    paused = False
    while(True):

        time.sleep(1)
        
        keys = key_check()

        if not paused:

            opt = random.randint(0,2)
            print (opt)
            
            if opt == 1:
                up()
                release()
            elif opt == 0:
                down()
                release()
            """    
            else:
                release()
            """
  

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                release()
                time.sleep(1)

main()       
