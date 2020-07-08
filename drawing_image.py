"""First, I’ll create blank image and then draw a line with cv2.line() 
We need to give the coordinates values for the starting point and the ending
 point then define the color of the line"""

import cv2
import numpy as np

# create a blank image 
img = np.zeros((512,512,3), np.uint8)

# Drawing lines
cv2.line(img,(0,0),(300,300), (0, 255, 0),5)

#Drawing a rectangle
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)

# Draw a Circle
cv2.circle(img,(400,50), 30,(255,255,0), 3)

# draw a diagonal line

cv2.line(img,(0,0),(img.shape[1], img.shape[0]),(0,255,0),3)

cv2.imshow("Blank Image", img)
cv2.waitKey(0)


