'''
cv2.putText(img, text, org(location), cv2.FONT, fontscale, color, thickness)
'''

import cv2

img = cv2.imread("learning/openCV/img2.jpg")
print(img.shape)
cv2.putText(img, "Senior Developer",(5700,3400),cv2.FONT_HERSHEY_COMPLEX, 10,(0,0,0), 30)

cv2.imshow("Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()