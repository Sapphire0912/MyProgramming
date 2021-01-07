import cv2
import numpy as np

img = cv2.imread('target.jpg')
modify = cv2.resize(img, (300, 300), interpolation = cv2.INTER_NEAREST)
cv2.imshow("img", img)
cv2.imshow("modify", modify)

cv2.waitKey(0)
