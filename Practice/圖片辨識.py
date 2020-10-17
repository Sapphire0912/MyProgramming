import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2

# img = cv2.imread('target.jpg') # 載入圖片
# print(type(img)) # <class 'numpy.ndarray'>
# print(img.shape) # (667, 1000, 3)

def matplot_show(img):
    plt.imshow(img, cmap = 'gray')
    plt.show()

# 偵測全身
path_fullbody = 'C:\\Users\\iris2\\AppData\\Local\\Programs\\Python\\Python37\\Lib\site-packages\\cv2\\data\\haarcascade_fullbody.xml'

body_classifier = cv2.CascadeClassifier(path_fullbody)

img = cv2.imread('target.jpg') # 載入圖片
result = cv2.imread('result2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # 用灰階開啟圖片
# print(gray.shape) # (667, 1000)

bodies = body_classifier.detectMultiScale(
    img,
    scaleFactor = 1.01,
    minNeighbors = 3,
    minSize = (150, 30)
)

# print(bodies)
# [[596 189 168 337]
#  [297  78 208 416]
#  [400  90 281 561]
#  [727 125 224 448]]

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)]
i = 0
for (x, y, w, h) in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), colors[i], 2)
    i += 1

# matplot_show(result)s

# def test(body):
#     x, y = body[:, 0], body[:, 1]
#     w, h = body[:, 2], body[:, 3]
#     x_w, y_h = x + w, y + h
#     plt.scatter(x, y, color = 'blue')
#     plt.scatter(x_w, y_h, color = 'red')
#     plt.show()

# test(bodies)

cv2.namedWindow('MyImg', cv2.WINDOW_NORMAL) # 讓視窗可以任意縮放大小
cv2.imshow("MyImg", img) # 顯示圖片
# cv2.imwrite('result2.jpg', img)
# matplot_show(gray)

# 按下任意建可關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
