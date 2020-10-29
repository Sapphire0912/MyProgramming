import cv2
import numpy as np

crop0 = cv2.imread("crop0.jpg") # 女
crop1 = cv2.imread("crop2.jpg") # 保全
crop2 = cv2.imread("crop3.jpg") # 男

crop0 = np.uint8(np.clip((0.8 * crop0 + 100), 0, 255))
cv2.imshow("crop0", crop0)

cv2.waitKey(0)