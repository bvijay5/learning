'''
blur = cv2.GaussianBlur(img, (kernal_size_x, kernal_size_y), sigma)
kernal_size can only be od like (3,3) or (5,5), etc
'''

import cv2

img = cv2.imread("learning/openCV/img2.jpg")

blur = cv2.GaussianBlur(img,(177,177), 0)

cv2.imshow("Orignal", img)
cv2.imshow("Blurred", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()