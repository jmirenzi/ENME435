# 03-09-2023
import numpy as np
import cv2

aa = 300; bb = 250; cc = 50

def snip_img(img):
    cv2.rectangle(img,(0,img.shape[0] - cc),(img.shape[1], img.shape[0] - aa), (0,0,255))
    return img[(img.shape[0] - aa):(img.shape[0] - cc), (0):(img.shape[1])]

def mask_image(img):
    mask = np.zeros((img.shape[0],img.shape[1]),dtype="uint8")
    pts = np.array([[90,img.shape[0]-25],[90,img.shape[0]-35],[img.shape[1]/2-30,100],[img.shape[1]/2+30,100],
                    [img.shape[1]-90,img.shape[0]-35],[img.shape[1]-90,img.shape[0]-25]],dtype=np.int32)
    cv2.fillConvexPoly(mask,pts,255)
    return cv2.bitwise_and(img,img,mask=mask)



if __name__ == "__main__":
    image = cv2.imread("testimage.jpg")
    cv2.imshow("image",image)
    cv2.imshow("snipped image",snip_img(image))
    cv2.imshow("masked image",mask_image(snip_img(image)))
    cv2.waitKey(0)
