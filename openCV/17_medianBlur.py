'''
blur = cv2.medianBlur(img, kernal_size)
Use black and whit image with spots
I am using normal image for practice
'''

import cv2

img = cv2.imread("learning/openCV/img.png")

blur = cv2.medianBlur(img, 77)

cv2.imshow("Orignal", img)
cv2.imshow("blurred", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
