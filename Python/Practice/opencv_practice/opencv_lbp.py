from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
import cv2
import numpy as np
import time


# Target: Using LBP algorithm and take out the road
# LBP algorithm (做分類器)
# 1. 原始圖片轉灰階且設定 blocks 大小 (3x3)  OK
# 2. 取正中間點的值當成 threshold, 和周圍的區域進行比較(i if region > threshold else 0)  OK
# 3. 將周圍的區域按照順時針或逆時針旋轉並且以二進制(8bits)轉成 10 進制相加後, 計算後的值為該中心點的 LBP 值  OK
# 4. 做卷積運算, 得到這張圖片的所有的 LBP 值  OK
# 5. 繪製直方圖, x軸為 0~255, y軸為出現次數
# 6. 將統計後的直方圖換成一個特徵向量(LBP 紋路特徵向量), 接著可用 SVM 等 ML 進行分類

# 單張圖片
# 1~4 都相同
# 5. 設定 cells 大小 (目前 10x10)
# 6. 根據 cells 大小迭代 LBP 值的圖片做出該 cells 的統計圖 (x, y 軸和分類器一樣)
# 7. 比較相鄰的 cells 是否相似, 相似則連接兩個區域, 否則反之
# 8. Ex. 描繪邊界


class MyLBP(object):
    def __init__(self, img):
        self.img = img
        self.y, self.x = img.shape
        self.size = None
        self.lbp_val = np.zeros(256, dtype=np.uint32)
        self.cells = None
        self.lbp_img = np.zeros(img.shape)


    def bit_to_int(self, bits_matrix):
        # 先處理 3x3
        # counterclockwise 逆時針
        # direction: 右下, 右, 右上, 上, 左上, 左, 左下, 下
        pos = np.array([[3, 4, 5], [2, 0, 6], [1, 0, 7]])
        weight = np.power(2, pos)
        lbp_value = np.sum(weight * bits_matrix) - 1
        return lbp_value

    def lbp(self, cells=10, r=1):
        self.size = 2 * r + 1

        con_img = np.zeros((self.y + 2, self.x + 2), dtype=np.uint16)
        con_img[1:self.y + 1, 1:self.x + 1] = self.img

        for j in range(0, self.y):
            for i in range(0, self.x):
                target_bits = con_img[j:j + self.size, i:i + self.size]
                # partial comparison, cells center: r, r
                target_bits = np.where(target_bits > target_bits[r, r], 1, 0)
                pixel_lbp = self.bit_to_int(target_bits)
                self.lbp_val[pixel_lbp] += 1

    def output_img(self, img, text):
        cv2.namedWindow(text, cv2.WINDOW_NORMAL)
        cv2.imshow(text, img)
        cv2.imwrite('%s.png' % text, img)

    def draw_histogram(self):
        x = np.arange(0, 256)
        plt.bar(x, self.lbp_val)
        plt.title("LBP Bar Chart")
        plt.xlabel("Gray Scale")
        plt.ylabel("Times")
        plt.ylim(0, np.max(self.lbp_val))
        plt.show()


path = "./road/road.jpg"
road = cv2.imread(path)

# use my lbp
# step1:
road_gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)

# step2 to 5:
st = time.time()
handle = MyLBP(road_gray)
handle.lbp()
print(np.sum(handle.lbp_val))
# handle.draw_histogram()
end = time.time()
print("spend time: ", end - st)
# spend time:  12.55710768699646 s


cv2.waitKey(0)
cv2.destroyAllWindows()
