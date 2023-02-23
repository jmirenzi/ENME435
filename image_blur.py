# 02-23-2023

import cv2
import numpy as np
import imutils


image = cv2.imread("landscape.jpeg")

cv2.imshow("unblurred",image)
blurred = cv2.blur(image,(13,13))
blurredG = cv2.GaussianBlur(image,(13,13),0)
blurredM = cv2.medianBlur(image,13)
cv2.imshow("blurred",blurred)
cv2.imshow("Gaussian blurred",blurredG)
cv2.imshow("Median blurred",blurredM)

cv2.waitKey(0)
