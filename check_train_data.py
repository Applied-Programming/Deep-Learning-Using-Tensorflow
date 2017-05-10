# check training data
import numpy as np
import cv2
from collections import Counter
from random import shuffle

train = np.load("final_training_data.npy")
print (len(train))

for i,data in enumerate(train):
    img = data[0]
    choice = data[1]

    if choice == [0,0,1]:
        cv2.imshow('check_training_data',img)
        print(str(i) + " " +str(choice))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
