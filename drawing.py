# 02-07-2023

import cv2
import numpy as np
import imutils

canvas = np.zeros((500,500,3),dtype="uint8")

cv2.line(canvas,(0,0),(200,400),(155,47,141),thickness=5)
cv2.imshow("canvas",canvas)

cv2.waitKey(0)