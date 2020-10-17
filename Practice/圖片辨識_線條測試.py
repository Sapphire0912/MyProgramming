# 線條測試
import numpy as np
import cv2

coord = np.array([
    [297, 78],
    [297, 494],
    [400, 661],
    [681, 661],
    [727, 573],
    [951, 573],
    [951, 125],
    [764, 189]
], np.int32) 

# coord 要重塑成 (頂點座標個數, 1, 2) 的陣列
coord = coord.reshape((-1, 1, 2))

img = cv2.imread('target.jpg')
cv2.polylines(img, [coord], True, (255, 0, 0), 4)
cv2.imshow("MyImg", img)
cv2.imwrite("result03.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()