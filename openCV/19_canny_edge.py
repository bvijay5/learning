import cv2

'''
edges = cv2.Canny(img, threshold1, threshold2)
'''

img = cv2.imread("learning/openCV/img.png", cv2.IMREAD_GRAYSCALE)


edges = cv2.Canny(img, 50,150)

cv2.imshow("Orignal", img)
cv2.imshow("Canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()