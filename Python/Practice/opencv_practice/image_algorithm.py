import cv2
import numpy as np
import time

# image source: https://www.pixiv.net/en/artworks/81438832
# the picture is for learning only
# all photos will be removed if copyright infringement
# mail: kotori228520@gmail.com


def output_img(img, text='My image'):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
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
        # print(b[0][0], g[0][0], r[0][0])  # 144 169 209
        gray = r*19595 + g*38469 + b*7472
        # print(gray[0][0])  # 11672584
        gray = np.right_shift(gray, 16).astype(np.uint8)  # 向右移 16 位元
        return gray

    def gaussian_filter(self, img):
        pass

    def sobel(self, img, dx=0, dy=0):
        gx_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        gy_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

        # method 1
        # 建立一個為0且大於原始圖片兩個pixel的陣列
        length, width = img.shape
        con_img = np.zeros((length+2, width+2), dtype=np.uint16)

        # 將圖像存入
        con_img[1:length+1, 1:width+1] = img

        # 暫時建立空陣列存放計算後的結果
        img_gx = np.zeros(img.shape, dtype=np.uint32)
        img_gy = np.zeros(img.shape, dtype=np.uint32)

        # 卷積(convolution)
        # dx 次數
        while dx > 0:
            for y_axis in range(0, length-1):
                for x_axis in range(0, width-1):
                    img_gx[y_axis][x_axis] = np.sum(con_img[y_axis:y_axis+3, x_axis:x_axis+3] * gx_kernel)
            dx -= 1
            con_img[1:length+1, 1:width+1] = img_gx

        # dy 次數
        while dy > 0:
            for y_axis in range(0, length-1):
                for x_axis in range(0, width-1):
                    img_gy[y_axis][x_axis] = np.sum(con_img[y_axis:y_axis+3, x_axis:x_axis+3] * gy_kernel)
            dy -= 1
            con_img[1:length+1, 1:width+1] = img_gy

        # 計算 sqrt(Gx^2 + Gy^2)
        result_img = np.sqrt(img_gx * img_gx + img_gy * img_gy).astype(np.uint8)
        return result_img


# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/rushia/rushia_ori.jpg"
rushia = cv2.imread(path)
# print(rushia.shape) # (1500, 1052, 3)

# use opencv
rushia_gray = cv2.cvtColor(rushia, cv2.COLOR_BGR2GRAY)
# output_img(rushia_gray, text="./rushia/rushia_gray")

rushia_gaussian = cv2.GaussianBlur(rushia_gray, (3, 3), 0)
# print(cv2.getGaussianKernel(3, 0))
# output_img(rushia_gaussian, text='./rushia/rushia_gray_gaussian_3x3')

rushia_sobel = cv2.Sobel(rushia_gray, ddepth=-1, dx=1, dy=1, ksize=3)
# print(rushia_sobel)
# output_img(rushia_sobel, text='./rushia/rushia_gray_sobel_dxdy_3x3')

# use my image algorithm
my_alg = MyImgAlg()
my_rushia_gray = my_alg.conv_to_gray(rushia)
# print(my_rushia_gray[0])
# print(my_rushia_gray.dtype)
# condition1: the type of image data output using the cv2.imshow() is np.uint8
# output_img(my_rushia_gray, "./rushia/rushia_my_alg_gray")

start_time = time.time()
my_rushia_sobel = my_alg.sobel(my_rushia_gray, dx=1, dy=1)
end_time = time.time()
output_img(my_rushia_sobel, text='./rushia/rushia_my_alg_sobel_dxdy')
print("cost time: ", end_time - start_time)  # cost time: 17.434980869293213 s <- dx dy
# cv2.imshow("my_sobel", my_rushia_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
