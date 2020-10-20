import cv2
import numpy as np

crop0 = cv2.imread("crop0.jpg") # 女
crop1 = cv2.imread("crop2.jpg") # 保全
crop2 = cv2.imread("crop3.jpg") # 男

# 輸出圖像
def show(img, text = 'test'):
    cv2.imshow(text, img)

# Pre. 轉成灰階
def cov_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. 消除雜訊
def blur_st(img, size = (9, 9), SD = 0):
    return cv2.GaussianBlur(img, size, SD)

# 2.1 邊緣檢測
def edge_detection(img, thres_min = 20, thres_max = 50):
    # gradX = cv2.Sobel(img, ddepth = ddepth, dx = 1, dy = 0, ksize = ksize)
    # gradY = cv2.Sobel(img, ddepth = ddepth, dx = 0, dy = 1, ksize = ksize)
    # gradient = cv2.subtract(gradX, gradY)
    # gradient = cv2.convertScaleAbs(gradient)
    # return gradient

    canny_ = cv2.Canny(img, thres_min, thres_max)
    return canny_

# 2.2 轉成二值圖
def threshold(img, thres_min = 90, thres_max = 255, method = cv2.THRESH_BINARY):
    _, thresh = cv2.threshold(img, thres_min, thres_max, method)
    return thresh

# 3.2 圖像形態學
def kernel_closed(thresh):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    return closed

# 3.3 細節刻畫
def detail(closed, iterations):
    closed = cv2.erode(closed, None, iterations = iterations)
    closed = cv2.dilate(closed, None, iterations = iterations)
    return closed

# 4. 描繪輪廓
def draw_contour(img, ori_crop):
    _, cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # result = cv2.drawContours(ori_crop, cnts, -1, (0, 0, 255), 2)
    print(cnts)
    # return result

gray0 = cov_gray(crop0)
gray1 = cov_gray(crop1)
gray2 = cov_gray(crop2)

blur0 = blur_st(gray0)
blur1 = blur_st(gray1)
blur2 = blur_st(gray2)

edge0 = edge_detection(blur0, 70, 100)
edge1 = edge_detection(blur1, 50, 160)
edge2 = edge_detection(blur2, 10, 150)

# thres0 = threshold(blur0)
# thres1 = threshold(blur1)
# thres2 = threshold(blur2)

# closed0 = kernel_closed(thres0)
# closed1 = kernel_closed(thres1)
# closed2 = kernel_closed(thres2)

# detail0 = detail(closed0, 6)
# detail1 = detail(closed1, 6)
# detail2 = detail(closed2, 5)

# draw0 = draw_contour(detail0, crop0)
# draw1 = draw_contour(detail1, crop1)
# draw2 = draw_contour(detail2, crop2)

show(edge0, "edge0")
show(edge1, "edge1")
show(edge2, "edge2")

cv2.waitKey(0)