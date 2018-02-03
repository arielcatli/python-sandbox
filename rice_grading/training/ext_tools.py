# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:53:16 2017

@author: Ariel Domingo Catli
"""

import cv2
import numpy as np
import imtransform as it

EXTRACT_LOADASGRAY = 0

def load_image(image_obj, size, colorMode = 1):
    image = it.resize(cv2.imread(image_obj, colorMode), height = size[0], width = size[1])
    return image

def main():
    image = load_image("cropped.jpg", [100,100], EXTRACT_LOADASGRAY)
    cv2.imshow("Sample", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    main()
    