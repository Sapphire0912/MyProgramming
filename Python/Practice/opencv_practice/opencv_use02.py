import cv2
import numpy as np

# Target: remove background and take out character or parrot
# image source: https://www.pixiv.net/en/artworks/81438832 <- rushia
# image source: https://www.pixiv.net/en/artworks/84349476 <- polka
# image source: myself <- pet
# the picture is for learning only
# all photos will be removed if copyright infringement
# mail: kotori228520@gmail.com


# Q. Whether the background difference can only distinguish unconnected objects?
def output_img(img, text):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)
    cv2.waitKey(0)
    cv2.destroyWindow(text)


# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/pet/pet_ori.jpg"
pet = cv2.imread(path)

