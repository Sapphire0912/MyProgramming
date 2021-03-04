import cv2
import numpy as np


def output_img(img, text = 'My image'):
    cv2.imshow(text, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# read image
path = "E:\\MyProgramming\\Python\\Practice\\opencv_practice\\fbk01.jpg"
fbk = cv2.imread(path)
output_img(fbk)

# turn into grayscale
fbk_gray = cv2.cvtColor(fbk, cv2.COLOR_BGR2GRAY)
output_img(fbk_gray)

