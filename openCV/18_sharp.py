'''
sharp = cv2.filter2D(img, depth, kernal)
depth = -1(to keep same as input)
kernal - >np.array
'''

import cv2
import numpy as np

img = cv2.imread("learning/openCV/img.png")

kernal = np.array([
    [0,-1,0],
    [-1,6,-1],
    [0,-1,0]
])

sharp = cv2.filter2D(img,-1, kernal)

cv2.imshow("orignal", img)
cv2.imshow("Sharp", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
