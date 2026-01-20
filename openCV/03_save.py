import cv2

#read
img = cv2.imread("learning/openCV/img.png")

# display
cv2.imshow("practice", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save edited img
cv2.imwrite("Edited.jpeg", img)

