# create_training_data.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
import win32con

def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array

    [None,UP,DOWN] boolean values.
    '''
    output = [0,0,0]
    
    UP = win32con.VK_UP
    DOWN = win32con.VK_DOWN
    
    '''
    None = [100]
    UP = [010]
    DOWN = [001]
    '''
    
    if UP in keys:
        output[1] = 1
    elif DOWN in keys:
        output[2] = 1
    else:
        output[0] = 1
    return output


file_name = 'training_data.npy'

up_pics = []

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []

def main():

    # Countdown
    for i in list(range(7))[::-1]:
        print(i+1)
        time.sleep(1)


    paused = False

    print("Training started!")
    
    while(True):

        if not paused:
            # (380,150,970,290) windowed mode to extract just the chrome://dino screen.
            screen = grab_screen(region=(380,150,970,290))
            #print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            # Scaling the image to 250x60
            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (250,60))
            
            keys = key_check()
            output = keys_to_output(keys)
            print(output)

            #if output == [0,1,0]:
            #    up_pics.append(screen)
            #np.save("UP_PICS.npy",up_pics)
            
            training_data.append([screen,output])
            if len(training_data) % 1000 == 0:
                print(len(training_data))
                np.save(file_name,training_data)

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


main()
