import cv2

img = cv2.imread("learning/openCV/img2.jpg")

w,h = img.shape[0:2]

center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(img, M, (h,w))

cv2.imshow("Orignal", img)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()