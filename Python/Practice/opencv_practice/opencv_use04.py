import cv2
import numpy as np

# image source: https://www.pixiv.net/en/artworks/81438832 <- rushia
# the picture is for learning only
# all photos will be removed if copyright infringement
# mail: kotori228520@gmail.com

# Target: Dynamic adjustment of image brightness and contrast
path = "E:/MyProgramming/Python/Practice/opencv_practice/rushia/rushia_ori.jpg"
rushia_ori = cv2.imread(path)
rushia_adj = cv2.imread(path)
alpha = 0
beta = 0


def updatealpha(x):
    global alpha, rushia_ori, rushia_adj
    alpha = cv2.getTrackbarPos('Alpha', 'Rushia')
    alpha = alpha * 0.05
    rushia_adj = np.uint8(np.clip((alpha * rushia_ori + beta), 0, 255))


def updatebeta(x):
    global beta, rushia_ori, rushia_adj
    beta = cv2.getTrackbarPos('Beta', 'Rushia')
    rushia_adj = np.uint8(np.clip((alpha * rushia_ori + beta), 0, 255))


cv2.namedWindow("Rushia", cv2.WINDOW_NORMAL)
cv2.createTrackbar('Alpha', 'Rushia', 0, 100, updatealpha)
cv2.createTrackbar('Beta', 'Rushia', 0, 255, updatebeta)
cv2.setTrackbarPos('Alpha', 'Rushia', 20)
cv2.setTrackbarPos('Beta', 'Rushia', 10)

while True:
    cv2.imshow('Rushia', rushia_adj)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
