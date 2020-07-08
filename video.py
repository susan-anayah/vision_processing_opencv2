import cv2
#How to read a  video and display it
cap = cv2.VideoCapture("Resources/tryvideo.mp4")

#diplay the video
while True:
    sucess, img = cap.read()

    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
