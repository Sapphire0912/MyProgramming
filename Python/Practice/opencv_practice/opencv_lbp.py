from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
import cv2
import numpy as np
import time


# Target: Using LBP algorithm and take out the road
# LBP algorithm
# 1. 原始圖片轉灰階且設定 blocks 大小 (3x3)  OK
# 2. 取正中間點的值當成 threshold, 和周圍的區域進行比較(i if region > threshold else 0)  OK
# 3. 將周圍的區域按照順時針或逆時針旋轉並且以二進制(8bits)轉成 10 進制相加後, 計算後的值為該中心點的 LBP 值  OK
# 4. 做卷積運算, 得到這張圖片的所有的 LBP 值  OK
# 5. 繪製直方圖, x軸為 0~255, y軸為出現次數 half
# 6. 將統計後的直方圖換成一個特徵向量(LBP 紋路特徵向量), 接著可用 SVM 等 ML 進行分類

def output_img(img, text):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)


def draw_histogram(lbp_val):
    x = np.arange(0, 256)
    plt.bar(x, lbp_val)
    plt.title("LBP Bar Chart")
    plt.xlabel("Gray Scale")
    plt.ylabel("Times")
    plt.ylim(0, 100000)
    plt.show()
    pass


def bit_to_int(bits_matrix):
    # 先處理 3x3
    # counterclockwise 逆時針
    # direction: 右下, 右, 右上, 上, 左上, 左, 左下, 下
    pos = np.array([[3, 4, 5], [2, 0, 6], [1, 0, 7]])
    weight = np.power(2, pos)
    lbp_value = np.sum(weight * bits_matrix)
    return lbp_value


def my_lbp(img, r=1):
    size = 2 * r + 1
    y, x = img.shape

    # 建立一個周圍填充0且大於圖片長寬 2pixel 的 array
    con_img = np.zeros((y+2, x+2), dtype=np.uint16)
    con_img[1:y+1, 1:x+1] = img

    lbp_val = np.zeros(256, dtype=np.uint32)

    # split image
    for j in range(0, y):
        for i in range(0, x):
            target_bits = con_img[j:j+size, i:i+size]
            # partial comparison, cells center: r, r
            target_bits = np.where(target_bits > target_bits[r, r], 1, 0)
            pixel_lbp = bit_to_int(target_bits)
            lbp_val[pixel_lbp] += 1

    draw_histogram(lbp_val)


path = "./road/road.jpg"
road = cv2.imread(path)

# use my lbp
# step1:
road_gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
# output_img(road_gray, text='./road/road_gray')

# step2 to 5:
st = time.time()
my_lbp(road_gray)
end = time.time()
# print(val, np.sum(val))
print("spend time: ", end - st)  # spend time:  12.55710768699646 s

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

cv2.waitKey(0)
cv2.destroyAllWindows()
