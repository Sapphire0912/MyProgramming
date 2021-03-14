import cv2


# Target: Using LBP algorithm and take out the road
def output_img(img, text):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)


path = "./road/road.jpg"
road = cv2.imread(path)

road_gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
# output_img(road_gray, text='./road/road_gray')


cv2.waitKey(0)
cv2.destroyAllWindows()
