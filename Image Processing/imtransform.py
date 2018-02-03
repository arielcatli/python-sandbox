# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 12:30:55 2017

@author: Ariel Domingo Catli
"""

#The module for image transformations

import cv2
import numpy as np

X_AXIS = 0
Y_AXIS = 1
XY_AXIS = -1

def shift(image, x_pixels, y_pixels):
    M = np.float32([[1,0,x_pixels],[0,1,y_pixels]])
    return cv2.warpAffine(image, M, (image.shape[1],image.shape[0]))

def rotate(image, degrees, center_rotation = None,  scale = 1.00):
    if center_rotation == None:
        M = cv2.getRotationMatrix2D((image.shape[1]//2, image.shape[0]//2), degrees, scale)
    else:
        M = cv2.getRotationMatrix2D(center_rotation, degrees, scale)
        
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

def resize(image, height = None, width = None, interpolation = cv2.INTER_AREA):
    
    if height == None and width == None:
        return image
    elif height == None and width != None:
        (w,h) = (width, int((width*image.shape[0])/(image.shape[1])))
    elif height != None and width == None:
        (w,h) = (int((image.shape[1]*height)/(image.shape[0])), height)
    else:
        (w,h) = (width, height)
        
    return cv2.resize(image, (w,h), interpolation)

def flip(image, axis):
    return cv2.flip(image, axis)
        
