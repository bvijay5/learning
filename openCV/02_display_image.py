import cv2

img = cv2.imread("learning/openCV/img.png")

if img is not None:
    cv2.imshow("Practice", img) #Opens the window
    cv2.waitKey(0) #wait till a key is pressed
    cv2.destroyAllWindows() #closs the window

else:
    print("Image not found")
