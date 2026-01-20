import cv2

img = cv2.imread("learning/openCV/img.png")

if img is not None:
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Practice", grey)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Img unable to load")

    