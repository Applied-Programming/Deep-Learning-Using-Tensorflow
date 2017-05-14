import numpy as np
import cv2
from collections import Counter
from random import shuffle
import imageio

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (250,160))

train = np.load("training_data.npy")
images = []
print (len(train))

for i,data in enumerate(train):
    img = data[0]
    choice = data[1]

    #if choice == [0,0,1]:

    # write the flipped frame
    #out.write(img)
    images.append(img)

        
    cv2.imshow('check_training_data',img)
    print(str(i) + " " +str(choice))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        imageio.mimsave('output.gif', images)
        break
    
