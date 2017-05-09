import numpy as np
from PIL import ImageGrab
import cv2
import time
from grabscreen import grab_screen
import win32con

def screen_record(): 
    last_time = time.time()
    
    while(True):
        # (380,150,970,290) windowed mode to extract just the chrome://dino screen.
        printscreen =  np.array(grab_screen((380,150,970,290)))
        #print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break    
screen_record()
