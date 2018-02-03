# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:35:56 2017

@author: Ariel Domingo Catli
"""

import numpy as np
import cv2 as c

img = np.zeros((512,512,3), np.uint8)
c.circle(img,(259,132),64,(0,0,255),-1)
c.circle(img,(259,132), 32, (0,0,0), -1)
c.circle(img,(192,255),64,(0,255,0), -1)
c.circle(img,(192,255),32,(0,0,0),-1)
pts = np.array([[259,132],[192,255],[327,255]], np.int32)
c.fillPoly(img,[pts],(0,0,0))
c.circle(img,(327,255),64, (255,0,0),-1)
c.circle(img,(327,255),32,(0,0,0),-1)
pts = np.array([[290,189],[327,255],[360,189]], np.int32)
c.fillPoly(img,[pts],(0,0,0))
c.imshow("Image",img)
c.waitKey(0)
c.destroyAllWindows()