import cv2

img = cv2.imread("learning/openCV/img.png")

print(img.shape[0:2])
new = cv2.rectangle(img,pt1=(1175,450), pt2=(1600,1100), color=(255,0,0), thickness=5)
cv2.imshow("New", new)
cv2.waitKey(0)
cv2.destroyAllWindows()
