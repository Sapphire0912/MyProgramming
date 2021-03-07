import cv2
import numpy as np


class MyImgAlg(object):
    def conv_to_gray(self, img):
        """原始公式: Gray = R*0.299 + G*0.587 + B*0.114
           使用 16 位精度計算 (2^16 = 65536)
           Gray = (R*19595 + G*38469 + B*7472) >> 16"""
        b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        b, g, r = b.astype(np.uint32), g.astype(np.uint32), r.astype(np.uint32)
        # print(b[0][0], g[0][0], r[0][0])  # 45 33 31
        gray = r*19595 + g*38469 + b*7472
        # print(gray[0][0])  # 2213162
        gray = np.right_shift(gray, 16)  # 向右移 16 位元
        gray = gray.astype(np.uint8)
        return gray

    def gaussian_filter(self, img):
        pass


# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/pet/pet_ori.jpg"
pet = cv2.imread(path)
# print(pet.shape)  # (1280, 960, 3)


# use opencv
pet_gray = cv2.cvtColor(pet, cv2.COLOR_BGR2GRAY)
# print(pet_gray[0])
cv2.imshow("cv2 gray", pet_gray)
cv2.imwrite("./pet/pet_cv2_gray.jpg", pet_gray)

# use my image algorithm
my_alg = MyImgAlg()
my_pet_gray = my_alg.conv_to_gray(pet)
# print(my_pet_gray[0])
# print(my_pet_gray.dtype)
# condition1: the type of image data output using the cv2.imshow() is np.uint8

cv2.imshow("My gray", my_pet_gray)
cv2.imwrite("./pet/pet_my_alg_gray.jpg", my_pet_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
