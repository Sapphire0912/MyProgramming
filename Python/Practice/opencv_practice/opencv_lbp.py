import cv2
import numpy as np


# Target: Using LBP algorithm and take out the road
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
            target_bits = img[j * size:(j + 1) * size, i * size:(i + 1) * size]
            # partial comparison, cells center: r, r
            target_bits = np.where(target_bits > target_bits[r, r], 1, 0)
            bit_to_int(target_bits)


path = "./road/road.jpg"
road = cv2.imread(path)

road_gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
# print(road_gray[0:6, 0:6])
# output_img(road_gray, text='./road/road_gray')

my_lbp(road_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()
