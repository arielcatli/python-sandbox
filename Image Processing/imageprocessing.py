#counting coins using Canny detection

import numpy as np
import cv2
import imtransform as it
from matplotlib import pyplot as plt

img = it.resize(cv2.imread("mask.jpg",0), height = 250)
img = cv2.medianBlur(img, 3)
cv2.imshow("Image", img)

blurred = cv2.GaussianBlur(img, (7,7), 0)
canny = cv2.Canny(blurred, 30, 150)

cv2.imshow("Contour Detection", np.hstack([img, blurred, canny]))

cnts = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("The image has", len(cnts[1]), "coins.")

img_copy = it.resize(cv2.imread("Sand.jpg"), height = 250)
cv2.drawContours(img_copy, cnts[1], -1, (0,0,255), 6)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img_copy,f'{len(cnts[1])} coins',(5,230), font, 1,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("Detected Coins", img_copy)

mask = np.zeros(img.shape[:2], np.uint8)

for (i, contour) in enumerate(cnts[1]):
    (x, y, w, h) = cv2.boundingRect(contour)
    coin = img[y:y+h, x:x+w]
    cv2.imshow(f'Coin No. {i+1}', coin)
    
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(contour)
    cv2.circle(mask, (int(centerX),int(centerY)), int(radius), 255, -1)
    
    in_mask = mask[y:y+h, x:x+w]
    cv2.imshow(f'Coin No. {i+1} - Masked', cv2.bitwise_and(coin, coin, mask = in_mask))

cv2.imshow("Mask Image", mask)


cv2.waitKey(0)
cv2.destroyAllWindows()