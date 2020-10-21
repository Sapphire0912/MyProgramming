import cv2
import numpy as np

class identify(object):
    def __init__(self, ori_img):
        self.ori_img = ori_img
        self.img = None
    
    def show(self, img, test):
        cv2.imshow(test, img)
    
    