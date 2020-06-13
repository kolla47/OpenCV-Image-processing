import cv2
import numpy as np

img = cv2.imread('bat.jpg')
#Averageing
blurImg = cv2.blur(img,(10,10))
cv2.imshow('blurred image',blurImg)
cv2.waitKey(0)
#Gausssian
kernek = (5,5)
gausblur = cv2.GaussianBlur(img, kernel,0)
cv2.imshow('Gaussian Blur', gausblur)
cv2.waitKey(0)
# Median blurring
medBlur = cv2.medianBlur(img,5)
cv2.imshow('Media Blurring', medBlur)
cv2.waitKey(0)
# Bilateral Filtering
bilFilter = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral Filtering', bilFilter)
cv2.waitKey(0)
cv2.destroyAllWindows()
