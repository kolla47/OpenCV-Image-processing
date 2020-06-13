import cv2
import numpy as np

img = cv2.imread('monarch',0)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img,(3,3),0)

# Apply Laplacian operator in some higher datatype
laplacian = cv2.Laplacian(blur,cv2.CV_64F)

cv2.imshow('LOG', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

