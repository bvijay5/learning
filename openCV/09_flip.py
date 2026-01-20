'''
cv2.flip(img, flipCode)
flipCode = 0 (top to bottom)
1 (left to right)
-1(both)
'''

import cv2

img = cv2.imread("learning/openCV/img2.jpg")

fliped0 = cv2.flip(img, 0)
fliped1 = cv2.flip(img, 1)
fliped_1 = cv2.flip(img, -1)

cv2.imshow("Orignal", img)
cv2.imshow("0", fliped0)
cv2.imshow("1", fliped1)
cv2.imshow("-1", fliped_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

