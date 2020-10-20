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

# 2. 邊緣檢測
def edge_detection(img, ddepth = cv2.CV_64F, ksize = -1):
    gradX = cv2.Sobel(img, ddepth = ddepth, dx = 1, dy = 0, ksize = ksize)
    gradY = cv2.Sobel(img, ddepth = ddepth, dx = 0, dy = 1, ksize = ksize)
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)
    return gradient

# 4. 描繪輪廓
def draw_contour(img, ori_crop):
    (_, cnts) = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # result = cv2.drawContours(ori_crop, cnts, -1, (0, 0, 255), 2)
    print(cnts)
    # return result

gray0 = cov_gray(crop0)
gray1 = cov_gray(crop1)
gray2 = cov_gray(crop2)

blur0 = blur_st(gray0)
blur1 = blur_st(gray1)
blur2 = blur_st(gray2)

edge0 = edge_detection(blur0)
edge1 = edge_detection(blur1)
edge2 = edge_detection(blur2)

# blur_0 = blur_st(edge0)
# blur_1 = blur_st(edge1)
# blur_2 = blur_st(edge2)

draw0 = draw_contour(edge0, crop0)
draw1 = draw_contour(edge1, crop1)
draw2 = draw_contour(edge2, crop2)

# show(draw0, "draw0")
# show(draw1, "draw1")
# show(draw2, "draw2")

cv2.waitKey(0)