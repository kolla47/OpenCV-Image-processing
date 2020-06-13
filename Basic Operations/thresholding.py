import cv2
import numpy as np

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray', img)

kernel = (5,5)
blur = cv2.GaussianBlur(img,kernel,0)
cv2.imshow('blur', blur)

ret,th = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
cv2.imshow('Adaptive Gaussian', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
