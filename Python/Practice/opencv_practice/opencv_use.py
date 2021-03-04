import cv2
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# visualize
sns.set()


# 目標去背景
def output_img(img, text='My image'):
    cv2.imshow(text, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# read image
path = "E:\\MyProgramming\\Python\\Practice\\opencv_practice\\fbk01.jpg"
fbk = cv2.imread(path)
# output_img(fbk)

# turn into grayscale
fbk_gray = cv2.cvtColor(fbk, cv2.COLOR_BGR2GRAY)
# output_img(fbk_gray)

# gaussian filter
fbk_gaussian = cv2.GaussianBlur(fbk_gray, (3, 3), 0)
# output_img(fbk_gaussian)

