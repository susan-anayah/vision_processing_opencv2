#Task 1. Blur an image
import cv2
import numpy as np
#reading the image
image = cv2.imread("Resources/header.jpg")

#cv2.imshow("original Image", image)
# #making it blur
# blurImage = cv2.blur(image,(10,10))
# cv2.imshow("Blurred image", blurImage)
# cv2.waitKey(0)

# # Task2. dilate  an image
# # Taking a matrix of size 5 as the kernel 
# kernel = np.ones((5,5), np.uint8) 
# img_dilation = cv2.dilate(image, kernel)
# cv2.waitKey(0)

# present the edges of the image

#calculate the edges using Canny edge algorithm

#plot the edges

imgCanny = cv2.Canny(image, 100,100)

cv2.imshow("edges", imgCanny)
cv2.waitKey(0)
