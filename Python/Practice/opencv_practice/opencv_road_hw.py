import cv2
import numpy as np


def nothing(x):
    pass


def output_img(img, text):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)


# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/road/road.jpg"
road = cv2.imread(path)
# print(road.shape)  # (1000, 1000, 3)

# convert to gray
gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
# output_img(gray, text="./road/gray")

# filter
blur = cv2.GaussianBlur(gray, (5, 5), 0)
# output_img(blur, text='./road/5x5blur')

# adjustment canny
# cv2.namedWindow("Canny")
# cv2.createTrackbar('thres1', 'Canny', 70, 255, nothing)
# cv2.createTrackbar('thres2', 'Canny', 210, 255, nothing)
#
# while True:
#     thres1 = cv2.getTrackbarPos('thres1', 'Canny')
#     thres2 = cv2.getTrackbarPos('thres2', 'Canny')
#     edge_canny = cv2.Canny(blur, thres1, thres2)
#     cv2.imshow('original', road)
#     cv2.imshow('Canny', edge_canny)
#     if cv2.waitKey(1) == ord('q'):
#         break

# sobel
sobel = cv2.Sobel(gray, ddepth=-1, dx=1, dy=0, ksize=3)
# output_img(sobel, text='./road/my_sobel_ddx')

# adjustment threshold
# cv2.namedWindow("threshold")
# cv2.createTrackbar('thres', 'threshold', 70, 255, nothing)
#
# while True:
#     thresh = cv2.getTrackbarPos('thres', 'threshold')
#     _, my_thres = cv2.threshold(sobel, thresh, 255, cv2.THRESH_BINARY)
#     cv2.imshow('original', sobel)
#     cv2.imshow('threshold', my_thres)
#     if cv2.waitKey(1) == ord('q'):
#         break

# threshold
_, thres = cv2.threshold(sobel, 30, 255, cv2.THRESH_BINARY)
# output_img(thres, text='./road/my_gray_thres_40_255')

# test
# edge_test = cv2.Canny(gray, 150, 255)
# output_img(edge_test, text='./road/gray_canny_150_255')

# line detention: HoughLines, HoughLinesP
# line_thres = 180
# lines = cv2.HoughLines(thres, 1, np.pi/180, line_thres)
# print(lines.shape)
#
# for line in lines:
#     for rho, theta in line:
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         x1 = int(x0 + 250*(-b))
#         x2 = int(x0 - 250*(-b))
#         y1 = int(y0 + 250*a)
#         y2 = int(y0 - 250*a)
#         cv2.line(road, (x1, y1), (x2, y2), (255, 0, 0), 2)

# HoughLinesP
line_thres = 326
min_line = 485
max_gap = 35
linesP = cv2.HoughLinesP(thres, 1, np.pi/180, threshold=line_thres, minLineLength=min_line, maxLineGap=max_gap)
# print(linesP.shape)
# print(linesP)

for line in [linesP[0], linesP[1]]:
    for x1, y1, x2, y2 in line:
        cv2.line(road, (x1, y1), (x2, y2), (255, 0, 0), 5)

cv2.imshow("Linear", road)
cv2.imwrite("./road/road_result.png", road)
cv2.waitKey(0)
cv2.destroyAllWindows()
