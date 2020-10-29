import cv2
import numpy as np

img1 = cv2.imread("crop0.jpg")
img2 = cv2.imread("crop1.jpg")
print(img1.shape)
print(img2.shape)
# result = np.hstack((img1, img2))
# cv2.imshow("result", result)