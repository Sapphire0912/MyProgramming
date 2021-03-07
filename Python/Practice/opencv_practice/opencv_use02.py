import cv2
import numpy as np

# Target: remove background and take out character or parrot
# image source: https://www.pixiv.net/en/artworks/81438832 <- rushia
# image source: https://www.pixiv.net/en/artworks/84349476 <- polka
# image source: myself <- pet
# the picture is for learning only
# all photos will be removed if copyright infringement
# mail: kotori228520@gmail.com


def output_img(img, text):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)
    cv2.waitKey(0)
    cv2.destroyWindow(text)


# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/rushia/rushia_ori.jpg"
rushia = cv2.imread(path)
# print(rushia.shape)  # (1500, 1052, 3)

# convert to grayscale
rushia_gray = cv2.cvtColor(rushia, cv2.COLOR_BGR2GRAY)
# output_img(rushia_gray, text="./rushia/rushia_gray")

# filter: gaussian filter
rushia_gaussian = cv2.GaussianBlur(rushia_gray, (3, 3), 0)
output_img(rushia_gaussian, text='./rushia/rushia_gray_gaussian')
