# Python program to explain cv2.erode() method  
  
# importing cv2  
import cv2 
  
# importing numpy  
import numpy as np 

# Reading an image in default mode  
image = cv2.imread("Resources/susan2.jpg")
  
# Window name in which image is displayed  
#window_name = 'Image'

# Displaying original image  
cv2.imshow("Read Image", image)
cv2.waitKey(0)
 
# Creating kernel 
kernel = np.ones((6, 6), np.uint8) 
  
# Using cv2.erode() method  
image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)  
  
# Displaying erode image  
cv2.imshow("erode image", image)  

cv2.waitKey(0)