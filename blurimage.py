import cv2
img = cv2.imread("Resources/header.jpg")

cv2.imshow("Image",img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (3,9), 0)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)

cv2.waitKey(0)