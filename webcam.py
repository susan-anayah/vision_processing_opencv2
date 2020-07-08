import cv2
#How  read a webcam and display it
webcam = cv2.VideoCapture(0)

#define the width and height
#3 = width, 4 = height

webcam.set(3.640)
webcam.set(4.480)

#diplay the webcam
while True:
    success, img = webcam.read()

    cv2.imshow("Webcam",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
