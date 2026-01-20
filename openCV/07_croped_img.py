import cv2

img = cv2.imread("learning/openCV/img.png")

cropped = img[450:1100,900:1800]   # [startY: endY, startX:endX]

print(img.shape)

cv2.imshow("Orignal pic", img)
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
