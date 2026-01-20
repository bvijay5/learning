import cv2

'''
cap = cv2.VideoCapture(soure)
source = 0/1
0 - inbuilt webcam
1 - external webcam
'''

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret: 
        print("Couldn't load video")
        break

    cv2.imshow("Web Cam", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        print("Quiting")
        break

cap.release()
cv2.destroyAllWindows()
