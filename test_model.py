# test_model.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, UP, DOWN
from getkeys import key_check
import random

print("Loaded Alexnet")
from alexnet import alexnet

WIDTH = 250
HEIGHT = 60
LR = 1e-3
EPOCHS = 5
MODEL_NAME = 'pydinoai-{}-{}-{}-epochs-2k-data.model'.format(LR, 'alexnetv2',EPOCHS)

t_time = 0.09

def up():
    PressKey(UP)
    ReleaseKey(DOWN)
    time.sleep(t_time)
    ReleaseKey(DOWN)
    
def down():
    PressKey(DOWN)
    ReleaseKey(UP)
    time.sleep(t_time)
    ReleaseKey(UP)

def release():
    ReleaseKey(DOWN)
    ReleaseKey(UP)
    
    
"""
def straight():
##    if random.randrange(4) == 2:
##        ReleaseKey(W)
##    else:
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(W)
    PressKey(A)
    #ReleaseKey(W)
    ReleaseKey(D)
    #ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(A)

def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    #ReleaseKey(W)
    #ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(D)
"""    
    
model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)
print("Loaded Alexnet")

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # (380,150,970,290) windowed mode to extract just the chrome://dino screen.
            screen = grab_screen(region=(380,150,970,290))
            #print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (WIDTH,HEIGHT))

            prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
            moves = list(np.around(prediction))
            print(moves, prediction)

            """
            thresh = .75

            if prediction[1] > thresh:
                up
            elif prediction[0] > thresh:
                down()
            else:
                release()
            """

            if moves == [1,0]:
                up()
            elif moves == [0,1]:
                down()
            else:
                release()

        keys = key_check()

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
