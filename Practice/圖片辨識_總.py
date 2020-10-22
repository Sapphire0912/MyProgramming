import cv2
import numpy as np

# 載入圖片後並裁切有人的部分
target = cv2.imread('target.jpg')
# 載入檔案
path_fullbody = 'C:\\Users\\iris2\\AppData\\Local\\Programs\\Python\\Python37\\Lib\site-packages\
\cv2\\data\\haarcascade_fullbody.xml' 
body_classifier = cv2.CascadeClassifier(path_fullbody) # 產生分類器
bodies = body_classifier.detectMultiScale(
    target,
    scaleFactor = 1.01,
    minNeighbors = 3,
    minSize = (150, 30)
) # 偵測全身人

# 裁切人的部分
crop = []
for (x, y, w, h) in bodies:
   crop.append(target[y:y + h, x:x + w])
# cv2.imshow("crop0", crop[0])
# cv2.imshow("crop1", crop[1])
# cv2.imshow("crop2", crop[2])
# cv2.imshow("crop3", crop[3])

# 儲存圖像
def write(img, text = 'test.jpg'):
    cv2.imwrite(text, img)

# 輸出圖像
def show(img, text = 'test.jpg'):
    cv2.imshow(text, img)

# Pre. 轉成灰階
def cov_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Pre. 調整亮度
def bright(img, alpha, beta):
    img = np.uint8(np.clip((alpha * img + beta), 0, 255))
    return img

# Pre. 圖像銳化
def contrast(img, ddepth = cv2.CV_64F, ksize = -1):
    gradX = cv2.Sobel(img, ddepth = ddepth, dx = 1, dy = 0, ksize = ksize)
    gradY = cv2.Sobel(img, ddepth = ddepth, dx = 0, dy = 1, ksize = ksize)
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)
    return gradient

# 1. 消除雜訊
def blur_st(img, size = (9, 9), SD = 0):
    return cv2.GaussianBlur(img, size, SD)

# 2.1 邊緣檢測
def edge_detection(img, thres_min = 20, thres_max = 50):
    canny_ = cv2.Canny(img, thres_min, thres_max)
    return canny_

# 2.2 轉成二值圖
def threshold(img, thres_min = 127, thres_max = 255, method = cv2.THRESH_BINARY):
    _, thresh = cv2.threshold(img, thres_min, thres_max, method)
    return thresh

# 3.2 圖像形態學
def kernel_closed(thresh, mor_method = cv2.MORPH_CLOSE):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    closed = cv2.morphologyEx(thresh, mor_method, kernel)
    return closed

# 3.3 細節刻畫
def detail(closed, iter_erode = 2, iter_dilate = 2):
    closed = cv2.erode(closed, None, iterations = iter_erode)
    closed = cv2.dilate(closed, None, iterations = iter_dilate)
    return closed

# 4. 描繪輪廓
def draw_contour(img, ori_crop):
    _, cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # result = cv2.drawContours(ori_crop, cnts, -1, (0, 0, 255), 2)
    # print(cnts)
    # return result

crop0 = cv2.imread("crop0.jpg") # 女
crop1 = cv2.imread("crop2.jpg") # 保全
crop2 = cv2.imread("crop3.jpg") # 男

# 轉成灰階
gray0 = cov_gray(crop0)
gray1 = cov_gray(crop1)
gray2 = cov_gray(crop2)
# show(gray0, "gray0")
# show(gray1, "gray1")
# show(gray2, "gray2")

# 高斯濾波
blur0 = blur_st(gray0)
blur1 = blur_st(gray1)
blur2 = blur_st(gray2)
# show(blur0, "blur0")
# show(blur1, "blur1")
# show(blur2, "blur2")
# write(blur0, "blur0.jpg")
# write(blur1, "blur1.jpg")
# write(blur2, "blur2.jpg")

# 銳化圖像
contrast0 = contrast(blur0)
contrast1 = contrast(blur1)
contrast2 = contrast(blur2)
# show(contrast0, "contrast0")
# show(contrast1, "contrast1")
# show(contrast2, "contrast2")
# write(contrast0, "contrast0.jpg")
# write(contrast1, "contrast1.jpg")
# write(contrast2, "contrast2.jpg")

# 轉二值圖
thres0 = threshold(contrast0)
thres1 = threshold(contrast1)
thres2 = threshold(contrast2)
# show(thres0, "thres0")
# show(thres1, "thres1")
# show(thres2, "thres2")
# write(thres0, "thres0.jpg")
# write(thres1, "thres1.jpg")
# write(thres2, "thres2.jpg")

# 圖像膨脹 & 收縮
kernel0 = threshold(thres0, cv2.MORPH_TOPHAT)
kernel1 = threshold(thres1, cv2.MORPH_OPEN)
kernel2 = threshold(thres2, cv2.MORPH_GRADIENT)
# show(kernel0, "kernel0")
# show(kernel1, "kernel1")
# show(kernel2, "kernel2")
# write(kernel0, "kernel0.jpg")
# write(kernel1, "kernel1.jpg")
# write(kernel2, "kernel2.jpg")

detail0 = detail(kernel0, iter_dilate = 1)
detail1 = detail(kernel1, 3)
detail2 = detail(kernel2)
# show(detail0, "detail0")
# show(detail1, "detail1")
# show(detail2, "detail2")
# write(detail0, "detail0.jpg")
# write(detail1, "detail1.jpg")
# write(detail2, "detail2.jpg")

edge0 = edge_detection(detail0)
edge1 = edge_detection(detail1)
edge2 = edge_detection(detail2)
show(edge0, "edge0")
show(edge1, "edge1")
show(edge2, "edge2")
# write(edge0, "edge0.jpg")
# write(edge1, "edge1.jpg")
# write(edge2, "edge2.jpg")


cv2.waitKey(0)
cv2.destroyAllWindows()