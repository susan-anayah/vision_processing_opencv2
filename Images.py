import cv2

#print('package is installed sucessfully')
#how to read an image and show
# img = cv2.imread("Resources/header.jpg")

# #show the image
# cv2.imshow("Read Image", img)
# cv2.waitKey(0)

#Converting an Image Grayscale
img = cv2.imread("Resources/header.jpg")


cv2.imshow("image",img)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", imgGray)

cv2.waitKey(0)




































































