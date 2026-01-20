'''
resized = cv2.resize(img, (w,h), fx,fy, interpolation)
'''

import cv2

img = cv2.imread("learning/openCV/img.png")

if img is None:
    print("Imagle not loaded")

else:
    resized = cv2.resize(img, (500,500))

    cv2.imshow("Orignal image", img)
    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
