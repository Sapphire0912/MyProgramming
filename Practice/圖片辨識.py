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
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # 用灰階開啟圖片
# print(gray.shape)

bodies = body_classifier.detectMultiScale(
    img,
    scaleFactor = 1.01,
    minNeighbors = 3,
    minSize = (150, 30)
)

for (x, y, w, h) in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.namedWindow('MyImg', cv2.WINDOW_NORMAL) # 讓視窗可以任意縮放大小
cv2.imshow("MyImg", img) # 顯示圖片
cv2.imwrite('result.jpg', img)
# matplot_show(gray)

# 按下任意建可關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
