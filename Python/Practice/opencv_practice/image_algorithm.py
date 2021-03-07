import cv2
import numpy as np


class MyImgAlg(object):
    def conv_to_gray(self, img):
        """原始公式: Gray = R*0.299 + G*0.587 + B*0.114
           使用 16 位精度計算 (2^16 = 65536)
           Gray = (R*19595 + G*38469 + B*7472) >> 16"""
        b, g, r = cv2.split(img)
        gray = (r*19595 + g*38469 + b*7472) >> 16
        return gray


# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/pet/pet_ori.jpg"
pet = cv2.imread(path)
# print(pet.shape)  # (1280, 960, 3)


# use opencv

# use my image algorithm

