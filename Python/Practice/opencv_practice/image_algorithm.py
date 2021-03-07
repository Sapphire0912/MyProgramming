import cv2
import numpy as np

# image source: https://www.pixiv.net/en/artworks/81438832 <- rushia
# the picture is for learning only
# all photos will be removed if copyright infringement
# mail: kotori228520@gmail.com


def output_img(img, text='My image'):
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)


class MyImgAlg(object):
    def conv_to_gray(self, img):
        """原始公式: Gray = R*0.299 + G*0.587 + B*0.114
           使用 16 位精度計算 (2^16 = 65536)
           Gray = (R*19595 + G*38469 + B*7472) >> 16"""
        b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        # 計算時要先把 dtype 整數型調高 否則會溢位
        b, g, r = b.astype(np.uint32), g.astype(np.uint32), r.astype(np.uint32)
        print(b[0][0], g[0][0], r[0][0])  # 144 169 209
        gray = r*19595 + g*38469 + b*7472
        print(gray[0][0])  # 11672584
        gray = np.right_shift(gray, 16).astype(np.uint8)  # 向右移 16 位元
        return gray

    def gaussian_filter(self, img):
        pass


# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/rushia/rushia_ori.jpg"
rushia = cv2.imread(path)

# use opencv
rushia_gray = cv2.cvtColor(rushia, cv2.COLOR_BGR2GRAY)
# output_img(rushia_gray, text="./rushia/rushia_gray")

rushia_gaussian = cv2.GaussianBlur(rushia_gray, (5, 5), 0)
output_img(rushia_gaussian, text='./rushia/rushia_gray_gaussian_5x5')

# use my image algorithm
my_alg = MyImgAlg()
my_rushia_gray = my_alg.conv_to_gray(rushia)
# print(my_rushia_gray[0])
# print(my_rushia_gray.dtype)
# condition1: the type of image data output using the cv2.imshow() is np.uint8
# output_img(my_rushia_gray, "./rushia/rushia_my_alg_gray")

cv2.waitKey(0)
cv2.destroyAllWindows()
