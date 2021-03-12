import cv2
import numpy as np


def adj_alpha(x):
    pass


def adj_beta(x):
    pass


def nothing(x):
    pass


def output_img(img, text):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)


# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/road/road.jpg"
road = cv2.imread(path)
road_adj = cv2.imread(path)
alpha = 0
beta = 0
# print(road.shape)  # (1000, 1000, 3)


# convert to gray
road_gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
# output_img(road_gray, text="./road/road_gray")

# Sobel
road_sobel = cv2.Sobel(road_gray, ddepth=-1, dx=1, dy=0, ksize=3)
# output_img(road_sobel, text="./road/road_sobel_dx_3")

# ----------
morph_kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
# dilate
road_dilate = cv2.dilate(road_gray, morph_kernel_cross)
# output_img(road_dilate, text="./road/road_dilate_cross_iter1")

# erode
road_erode = cv2.erode(road_gray, morph_kernel_cross)
# output_img(road_erode, text="./road/road_erode_cross_iter1")

# absdiff
road_bg_diff = cv2.absdiff(road_dilate, road_erode)
# output_img(road_bg_diff, text="./road/road_bg_diff")

# adjustment threshold
# cv2.namedWindow("adjustment threshold", cv2.WINDOW_NORMAL)
# cv2.createTrackbar("thres", "adjustment threshold", 0, 255, nothing)
# while True:
#     thres_bar = cv2.getTrackbarPos("thres", "adjustment threshold")
#     _, road_thres = cv2.threshold(road_bg_diff, thres_bar, 255, cv2.THRESH_BINARY)
#     cv2.imshow("adjustment threshold", road_thres)
#
#     if cv2.waitKey(10) & 0xFF == ord("q"):
#         break

# test
_, road_thres = cv2.threshold(road_bg_diff, 55, 255, cv2.THRESH_BINARY)
# output_img(road_thres, text="./road/road_thres_55_255")

# adjustment of image brightness and contrast





# draw contour
# road_contour, road_hierarchy = cv2.findContours(road_thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# road_draw_contour = cv2.drawContours(road.copy(), road_contour, -1, (0, 0, 255), 3)
# output_img(road_draw_contour, text="./road/road_draw_contour")


cv2.waitKey(0)
cv2.destroyAllWindows()
