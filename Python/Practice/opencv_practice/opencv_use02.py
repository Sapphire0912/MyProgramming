import cv2
import numpy as np

# Target: remove background and take out character or parrot
# image source: https://www.pixiv.net/en/artworks/81438832 <- rushia
# image source: https://www.pixiv.net/en/artworks/84349476 <- polka
# image source: myself <- pet
# the picture is for learning only
# all photos will be removed if copyright infringement
# mail: kotori228520@gmail.com

# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/rushia/rushia_ori.jpg"
rushia = cv2.imread(path)
# print(rushia.shape)  # (1500, 1052, 3)
