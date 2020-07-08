#writing on an image
#define the text
#define the text to be written
#define the font 

import cv2
#import numpy as np

#to create a blank image
#img = np.zeros(shape=[512, 512, 3], dtype=np.uint8  

#call an image in the directory
img = cv2.imread('Resource/Tombraider.jpg')

position = (100,50)
cv2.putText(
     img, #image on which text is written
     "This is a tomb raider image", #text
     position, #position at which writing has to start
     cv2.FONT_HERSHEY_COMPLEX, #font family
     1, #font size
     (0, 0, 255), #font color
     3) #font stroke
cv2.imshow('Read Image', img)
cv2.waitKey(0)