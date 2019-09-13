import cv2
import time
import numpy as np

def print_position(height, width, position, fps):
    print("fps:", fps, position)
    local_x = int((position[0]/width)*50)
    local_y = int((position[1]/height)*15)
    print("-"*52)
    for i in range(15):
        print("|",end="")
        for j in range(50):
            if local_x == j and local_y == i:
                print("*",end="")
            else:
                print(" ",end="")
        print("|")
    print("-"*52)
