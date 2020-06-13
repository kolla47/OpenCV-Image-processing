import cv2
import numpy as np

img = cv2.imread('cat.png',0)
ksize=5
sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize)
sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize)

cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
