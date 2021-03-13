import cv2
import numpy as np


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

# convert to gray
gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
# output_img(gray, text="./road/gray")

# filter
blur = cv2.GaussianBlur(gray, (5, 5), 0)
output_img(blur, text='./road/5x5blur')



cv2.waitKey(0)
cv2.destroyAllWindows()
