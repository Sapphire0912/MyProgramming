from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
import cv2
import numpy as np
import time


# Target: Using LBP algorithm and take out the road
# LBP algorithm
# 1. 原始圖片轉灰階且設定 blocks 大小 (3x3)
# 2. 取正中間點的值當成 threshold, 和周圍的區域進行比較(i if region > threshold else 0)
# 3. 將周圍的區域按照順時針或逆時針旋轉並且以二進制(8bits)轉成 10 進制相加後, 計算後的值為該中心點的 LBP 值
# 4. 做卷積運算, 得到這張圖片的所有的 LBP 值
# 5. 繪製直方圖, x軸為 0~255, y軸為出現次數
# 6. 將統計後的直方圖換成一個特徵向量(LBP 紋路特徵向量), 接著可用 SVM 等 ML 進行分類

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

cv2.waitKey(0)
cv2.destroyAllWindows()
