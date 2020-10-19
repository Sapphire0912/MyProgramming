import numpy as np
import cv2
import matplotlib as mpt
import matplotlib.pyplot as plt


ori = cv2.imread("target.jpg")
ori_gray = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)
# cv2.imshow("ori_gray", ori_gray)

blurred = cv2.GaussianBlur(ori_gray, (9, 9), 0)
# cv2.imshow("blurred_first", blurred)

# 用 Sobel 計算 x, y方向上的梯度, 接著在 x 方向減去 y 方向的梯度 
gradX = cv2.Sobel(ori_gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
gradY = cv2.Sobel(ori_gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
# cv2.imshow("gradient1", gradient)

# 去除圖片的雜訊
blurred = cv2.GaussianBlur(gradient, (9, 9), 0)
(_, thresh) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("thresh", thresh)

# 用二值化強調物件圖形
item1 = cv2.dilate(thresh, None, iterations = 6)
item1 = cv2.erode(thresh, None, iterations = 10)
item1 = cv2.dilate(thresh, None, iterations = 2)
cv2.imshow("item", item1)

# 加上邊框
# _, cnts = cv2.findContours(item1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
# rect = cv2.minAreaRect(c)
# box = np.int0(cv2.boxPoints(rect))
# draw_img = cv2.drawContours(ori.copy(), [box], -1, (0, 0, 255), 3)
# cv2.imshow("last1", draw_img)


cv2.waitKey(0)
cv2.destroyAllWindows()