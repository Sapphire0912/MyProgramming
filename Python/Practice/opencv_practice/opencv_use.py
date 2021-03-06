import cv2


# 目標去背景 取出 fbk
def output_img(img, text='My image'):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)
    cv2.waitKey(0)
    cv2.destroyWindow(text)


# read image
path = "E:\\MyProgramming\\Python\\Practice\\opencv_practice\\fbk01.jpg"
fbk = cv2.imread(path)
B, G, R = cv2.split(fbk)
# print(B)
# output_img(fbk)

# turn into grayscale
fbk_gray = cv2.cvtColor(fbk, cv2.COLOR_BGR2GRAY)
# output_img(fbk_gray, text='fbk_gray')

# filter: gaussian filter
fbk_gaussian = cv2.GaussianBlur(fbk_gray, (3, 3), 0)
# output_img(fbk_gaussian, text='fbk_gaussian_3x3')

# edge detection: Sobel
fbk_sobel = cv2.Sobel(fbk_gaussian, ddepth=-1, dx=1, dy=0, ksize=3)
# output_img(fbk_sobel, text='fbk_gaussian_sobel_dx_3x3')

# edge detection: Canny
fbk_canny = cv2.Canny(fbk_gaussian, 70, 210)
# output_img(fbk_canny, text='fbk_gaussian_canny_70_210')

# threshold(use gray)
# _, fbk_thres = cv2.threshold(fbk_gray, 150, 255, cv2.THRESH_BINARY)
# output_img(fbk_thres, text='fbk_gray_threshold_135_255')

# morphology: create kernel
morph_kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
morph_kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
morph_kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

# ----------
# morphology: dilate
fbk_dilate = cv2.dilate(fbk, morph_kernel_cross, 5)
# output_img(fbk_dilate, text='fbk_dilate_cross_iteration_5')

# morphology: erode
fbk_erode = cv2.erode(fbk, morph_kernel_cross, 5)
# output_img(fbk_erode, text='fbk_erode_cross_iteration_5')

# background difference
fbk_absdiff = cv2.absdiff(fbk_dilate, fbk_erode)
# output_img(fbk_absdiff, text='fbk_cross_iter5_absdiff_dilate-erode')

# threshold(use absdiff)
_, fbk_thres = cv2.threshold(fbk_absdiff, 60, 255, cv2.THRESH_BINARY)
# output_img(fbk_thres, text='fbk_cross_absdiff_thres_60_255')

# pixel reversal
fbk_reverse = cv2.bitwise_not(fbk_thres)
# output_img(fbk_reverse, text='fbk_cross_absdiff_thres_60_255_pixel_reverse')

# draw contour


# test
# fbk_iter1 = cv2.imread("E:\\MyProgramming\\Python\\Practice\\opencv_practice\\fbk_cross_absdiff_dilate-erode.jpg")
# fbk_iter5 = cv2.imread("E:/MyProgramming/Python/Practice/opencv_practice/fbk_cross_iter5_absdiff_dilate-erode.jpg")

# fbk_iter_absdiff = cv2.absdiff(fbk_iter5, fbk_iter1)
# cv2.error size.width > 0; So these two graphs are the same
# output_img(fbk_iter_absdiff, text='fbk_iter_absdiff_with_5_1')
