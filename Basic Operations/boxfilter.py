import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('panda1.jpg',0)
x = int(input())

kernel = np.ones((x,x),np.float32)/pow(x,2)
boxfil = cv2.boxFilter(img,0,(x,x),img,(-1,-1),False,cv2.BORDER_DEFAULT)
cv2.imshow('Filtered', boxfil)
cv2.waitKey()
cv2.destroyAllWindows()
