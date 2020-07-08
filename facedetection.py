import cv2

color = (255, 255, 0)

#add our cascade
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

#Read the image
img = cv2.imread("Resources/faces.jpg")

#resize the image
imResize = cv2.resize(img, (600,400))

#Convert to grayscale
imgGray = cv2.cvtColor(imResize, cv2.COLOR_BGR2GRAY)

#Find the faces in the image provided
#define the scale factor
#define the minimum neighbour
face = faceCascade.detectMultiScale(imgGray,1.1,4)

#lastly create a bounding box across the detected faces
#looping over every image
#starting point
#corner points

for (x,y,w,h) in face:
    #draw a bounding box
    
    cv2.rectangle(imResize, (x,y), (x+w, y+h), color,2)
    #input text"face"
    cv2.putText(imResize, "face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 1, color,1)

cv2.imshow("Faces", imResize)
cv2.waitKey(0)
