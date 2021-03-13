import cv2
import numpy as np


def adj_alpha(x):
    global alpha, road, road_adj
    alpha = cv2.getTrackbarPos("alpha", "adjustment brightness and contrast")
    alpha = alpha * 0.02
    road_adj = np.uint8(np.clip((alpha * road + beta), 0, 255))


def adj_beta(x):
    global beta, road, road_adj
    beta = cv2.getTrackbarPos("beta", "adjustment brightness and contrast")
    road_adj = np.uint8(np.clip((alpha * road + beta), 0, 255))


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

# adjustment of image brightness and contrast
road_adj = cv2.imread(path)
alpha = 0
beta = 0
# cv2.namedWindow("adjustment brightness and contrast", cv2.WINDOW_NORMAL)
# cv2.createTrackbar("alpha", "adjustment brightness and contrast", 0, 250, adj_alpha)
# cv2.createTrackbar("beta", "adjustment brightness and contrast", 0, 255, adj_beta)
# cv2.setTrackbarPos("alpha", "adjustment brightness and contrast", 50)
# cv2.setTrackbarPos("beta", "adjustment brightness and contrast", 0)
#
# while True:
#     cv2.imshow("adjustment brightness and contrast", road_adj)
#     if cv2.waitKey(1) == ord('q'):
#         break

# test
# road_test = np.uint8(np.clip((1.4 * road + 20), 0, 255))
# output_img(road_test, text="./road/road_test")

# convert to gray
road_gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
# output_img(road_gray, text="./road/road_test_gray")

# gaussian filter
road_gaussian = cv2.GaussianBlur(road_gray, (5, 5), 0)
# output_img(road_gaussian, text='./road/road_gaussian_5x5')

# Sobel
road_sobel = cv2.Sobel(road_gray, ddepth=-1, dx=1, dy=0, ksize=3)
# output_img(road_sobel, text="./road/road_sobel_dx_3")

# Canny
road_canny = cv2.Canny(road_gaussian, 90, 210)
output_img(road_canny, text="./road/road_gaussian_canny_90_210")

# ----------
morph_kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
# dilate
# road_dilate = cv2.dilate(road_canny, morph_kernel_cross, iterations=3)
# output_img(road_dilate, text="./road/road_canny_dilate_cross_3x3_iter3")

# erode
road_erode = cv2.erode(road_gray, morph_kernel_cross)
# output_img(road_erode, text="./road/road_canny_erode_cross_3x3_iter1")

# absdiff
# road_bg_diff = cv2.absdiff(road_dilate, road_erode)
# output_img(road_bg_diff, text="./road/road_canny_bg_diff_3x3_kernel")

# adjustment threshold
# cv2.namedWindow("adjustment threshold", cv2.WINDOW_NORMAL)
# cv2.createTrackbar("thres", "adjustment threshold", 0, 255, nothing)
# while True:
#     thres_bar = cv2.getTrackbarPos("thres", "adjustment threshold")
#     _, road_thres = cv2.threshold(road_dilate, thres_bar, 255, cv2.THRESH_BINARY)
#     cv2.imshow("adjustment threshold", road_thres)
#
#     if cv2.waitKey(1) == ord("q"):
#         break

# test
# _, road_thres = cv2.threshold(road_canny, 55, 255, cv2.THRESH_BINARY)
# output_img(road_thres, text="./road/road_canny_130_210_thres_55_255_3x3_kernel")

# linear tracking
rho = 1
theta = np.pi/180
threshold = 80
min_line_length = 1
max_line_gap = 20
line_image = road.copy()
lines = cv2.HoughLinesP(road_canny, rho, theta, threshold, min_line_length, max_line_gap)
print(lines.shape)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)


# draw contour
# road_contour, road_hierarchy = cv2.findContours(road_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# road_draw_contour = cv2.drawContours(road.copy(), road_contour, -1, (0, 0, 255), 3)
# output_img(road_draw_contour, text="./road/road_canny_draw_contour")

cv2.imshow("linear track", line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
