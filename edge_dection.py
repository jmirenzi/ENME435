# 03-14-2023

import cv2
import numpy as np
import imutils

def thres_image(img):
    # threshold something else
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    yellowLower = np.array([0, 65, 164]); yellowUpper = np.array([255, 255, 255])
    whiteLower = np.array([0, 0, 208]); whiteUpper = np.array([255, 255, 255])
    yellow_mask = cv2.inRange(hsv, yellowLower, yellowUpper); white_mask = cv2.inRange(hsv, whiteLower, whiteUpper)
    full_mask = cv2.bitwise_or(yellow_mask, white_mask)
    frame = cv2.bitwise_or(gray, full_mask)
    thresh = 180
    frame = cv2.threshold(frame, thresh, 255, cv2.THRESH_BINARY)[1]
    return frame


if __name__ == "__main__":
    img = cv2.imread("coins-stock.jpg")
    scale=.75
    dim = (int(img.shape[1]*scale),int(img.shape[0]*scale))
    frame = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
    thres = thres_image(frame)
    blurred = cv2.GaussianBlur(frame,(5,5),0)
    edged = cv2.Canny(blurred,40,150)

    cv2.imshow("original",frame)
    cv2.imshow("blurred",blurred)
    cv2.imshow("edges",edged)

    cv2.waitKey(0)