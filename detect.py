import cv2
import time
import numpy as np
 
def detect(img):
    _, g, r = cv2.split(img)
    red_map = r
    # print(red_map)   
    (_, max_val, _, max_loc) = cv2.minMaxLoc(red_map)
    # print("max value", max_val)
    return max_loc

if __name__ == '__main__' :
    pass