# Python program to explain cv2.erode() method  
  
# importing cv2 and numpy 
import cv2 
import numpy as np
# Reading an image in default mode 
img = cv2.imread("Resources/header.jpg") 

# show original image
cv2.imshow("Read Image", img)


# Creating kernel 
kernel = np.ones((5, 5), np.uint8) 
  
# Using cv2.erode() method  
img = cv2.erode(img, kernel, iterations=3)  
  
# Displaying the eroded image  
cv2.imshow("erode image", img) 
cv2.waitKey(0) 