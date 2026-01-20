import cv2

img = cv2.imread("learning/openCV/img.png")

h,w,c = img.shape
print(f"Height: {h}\nWidth: {w}\nChannels:{c}")
