import numpy as np
import cv2

# img = cv2.imread('target.jpg') # 載入圖片
# print(type(img)) # <class 'numpy.ndarray'>
# print(img.shape) # (667, 1000, 3)

# 偵測全身
path_fullbody = 'C:\\Users\\iris2\\AppData\\Local\\Programs\\Python\\Python37\\Lib\site-packages\\cv2\\data\\haarcascade_fullbody.xml'
# path_fullbody = 'C:\\Users\\kotori\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_fullbody.xml'
body_classifier = cv2.CascadeClassifier(path_fullbody)
img = cv2.imread('target.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
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

crop = []
for (x, y, w, h) in bodies:
   crop.append(img[y:y + h, x:x + w])
result = np.uint8(np.clip((0.8 * crop[0] + 60), 0, 255))
cv2.imshow("Test0", result)


cv2.waitKey(0)
cv2.destroyAllWindows()
