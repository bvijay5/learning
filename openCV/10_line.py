'''
cv2.line(img, pt1, pt2, color, thickness)
'''

import cv2

img = cv2.imread("learning/openCV/img2.jpg")

print(img.shape[0:2])

new_img = cv2.line(img, pt1=(500,500), pt2=(5000,9000), color=(255,150,0), thickness=100)

cv2.imshow("Line", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()