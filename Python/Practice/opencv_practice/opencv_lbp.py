from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
import cv2
import numpy as np
import time


# Target: Using LBP algorithm and take out the road
# LBP algorithm
# 1. 原始圖片轉灰階且設定 cells 大小 OK
# 2. 將灰階圖片依照 cells 大小切割後, 切割後的正中間為中心點當成 threshold OK
# 3. 選擇鄰近區域要依順時針或逆時針旋轉, 若值大於 threshold 給 1 否則 0 (1 if region > threshold else 0) OK
# 4. 接著按照旋轉方向取 2進制 轉成 10進制 後的值 OK
# 5. 繪製直方圖 ???

def output_img(img, text):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)


def bit_to_int(bits_matrix):
    # 先處理 3x3
    # counterclockwise 逆時針
    # direction: 右下, 右, 右上, 上, 左上, 左, 左下, 下
    pos = np.array([[3, 4, 5], [2, 0, 6], [1, 0, 7]])
    weight = np.power(2, pos)
    lbp_value = np.sum(weight * bits_matrix)

    print(lbp_value)


def my_lbp(img, r=1):
    size = 2 * r + 1
    y, x = img.shape

    # split image
    for j in range(0, y // size):
        for i in range(0, x // size):
            target_bits = img[j*size:(j+1)*size, i*size:(i+1)*size]
            # partial comparison, cells center: r, r
            target_bits = np.where(target_bits > target_bits[r, r], 1, 0)
            bit_to_int(target_bits)


path = "./road/road.jpg"
road = cv2.imread(path)

road_gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
# print(road_gray[0:6, 0:6])
# output_img(road_gray, text='./road/road_gray')

# use my lbp
# st = time.time()
# my_lbp(road_gray)
# end = time.time()
# print("cost time: ", end - st)  # cost time:  2.0037386417388916 s

# ----------
# use scikit-image module lbp
# use matplotlib imshow lbp image
radius = 1
n_points = 8 * radius

# lbp method returns the dtype and value of the image(current only the image)
# default: dtype float64, value 0 to 255
# ror: dtype float64, value 0 to 255
# nri_uniform: dtype float64, value 0 to 58
# uniform: dtype float64, value 0 to 9
# var: dtype float64, value has han

lbp = local_binary_pattern(road_gray, n_points, radius, method='var')
# print(lbp[30:40, 790:800])
# print(np.max(lbp), np.min(lbp))
# plt.imshow(lbp, cmap='gray')
# plt.show()

# output_img(lbp, text="./road/road_lbp_var")

# image 無法儲存
# edges = filters.sobel(road_gray)
# output_img(edges, text="./road/road_skimage_sobel")

cv2.waitKey(0)
cv2.destroyAllWindows()
