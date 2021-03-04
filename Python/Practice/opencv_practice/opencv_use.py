import cv2
import numpy as np

# read image
path = "E:\\MyProgramming\\Python\\Practice\\opencv_practice\\fbk01.jpg"
fbk = cv2.imread(path)
print(fbk.shape)


# output image
cv2.imshow('my image', fbk)
cv2.waitKey(0)
cv2.destroyAllWindows()
