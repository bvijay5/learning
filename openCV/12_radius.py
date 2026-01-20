import cv2

'''
cv2.circle(img, center, radius, color, thickness)
'''

img = cv2.imread("learning/openCV/img.png")

c = cv2.circle(img, (1375,780), 300, (255,0,0), -1)

cv2.imshow("Circle", c)
cv2.waitKey(0)
cv2.destroyAllWindows()

