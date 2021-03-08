import cv2

# image source: myself
# the picture is for learning only
# all photos will be removed if copyright infringement
# mail: kotori228520@gmail.com


# Q. Whether the background difference can only distinguish unconnected objects?
def output_img(img, text):
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.imshow(text, img)
    cv2.imwrite('%s.png' % text, img)
    # cv2.waitKey(0)
    # cv2.destroyWindow(text)


# read image
path = "E:/MyProgramming/Python/Practice/opencv_practice/pet/pet_ori.jpg"
pet = cv2.imread(path)
# print(pet.shape)  # (1280, 960, 3)

# convert to gray
pet_gray = cv2.cvtColor(pet, cv2.COLOR_BGR2GRAY)
# output_img(pet_gray, text="./pet/pet_gray")

# gaussian filter
pet_gaussian = cv2.GaussianBlur(pet_gray, (3, 3), 0)
# output_img(pet_gaussian, text="./pet/pet_gaussian")

# sobel
pet_sobel = cv2.Sobel(pet_gaussian, ddepth=-1, dx=2, dy=0, ksize=5)
# output_img(pet_sobel, text='./pet/pet_sobel_ddx_ksize_5')

# canny
pet_canny = cv2.Canny(pet_gaussian, 70, 210, apertureSize=3, L2gradient=True)
output_img(pet_canny, text='./pet/pet_canny_70_210_aperture_3_L2')


# use background difference
morph_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
# dilate
pet_dilate = cv2.dilate(pet_gaussian, morph_kernel)
# output_img(pet_dilate, text='./pet/pet_dilate')
# erode
pet_erode = cv2.erode(pet_gaussian, morph_kernel)
# output_img(pet_erode, text='./pet/pet_erode')
# absdiff
pet_absdiff = cv2.absdiff(pet_dilate, pet_erode)
# output_img(pet_absdiff, text='./pet/pet_absdiff')
# print(pet_absdiff.shape)  # (1280, 960)

# threshold
_, pet_thres = cv2.threshold(pet_absdiff, 75, 255, cv2.THRESH_BINARY)
# output_img(pet_thres, text='./pet/pet_thres_75_255_binary')

cv2.waitKey(0)
cv2.destroyAllWindows()
# Q. How to solve the problem of too bright objects
