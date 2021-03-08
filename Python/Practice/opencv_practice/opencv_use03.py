import cv2

# image source: https://www.pixiv.net/en/artworks/84349476 <- polka
# the picture is for learning only
# all photos will be removed if copyright infringement
# mail: kotori228520@gmail.com

# Target: remove background and take out polka
# try to use dynamic adjustment parameters


def nothing(x):
    pass


def img_morph(img):
    pass


def img_handle(path):
    # read image
    polka = cv2.imread(path)

    # convert to grayscale
    polka_gray = cv2.cvtColor(polka, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow("Polka", cv2.WINDOW_NORMAL)
    cv2.createTrackbar("threshold", "Polka", 0, 255, nothing)

    while True:
        my_thres = cv2.getTrackbarPos("threshold", "Polka")
        _, polka_thres = cv2.threshold(polka_gray, my_thres, 255, cv2.THRESH_BINARY)
        cv2.imshow("Polka", polka_thres)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


def main():
    path = "E:/MyProgramming/Python/Practice/opencv_practice/polka/polka_ori.jpg"
    img_handle(path)


if __name__ == "__main__":
    main()

