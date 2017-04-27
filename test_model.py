# test_model.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, UP, DOWN
from getkeys import key_check
import random

print("Loading Alexnet...")
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
    
model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)
print("Loaded Alexnet.")

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
            fwd_thresh = 0.70

            #if prediction[0] > fwd_thresh:
            #    straight()
            
            if prediction[1] > thresh:
                up()
            elif prediction[2] > thresh:
                down()
            else:
                release()
            """

            if moves == [0,1,0]:
                print("Jump")
                up()
            elif moves == [0,0,1]:
                print("Duck")
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
