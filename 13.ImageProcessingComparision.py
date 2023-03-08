import cv2
import numpy as np
import os

img = cv2.imread('onion.PNG')
cv2.imshow("original Image", img)

kernel = np.ones((5,5),np.uint8)

# convert to gray
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image',img_gray)


# convert to blur
img_blur = cv2.GaussianBlur(img_gray,(7,7),0)
cv2.imshow('Blur Image', img_blur)


# finding edges using canny functions
img_canny = cv2.Canny(img,200,200)
cv2.imshow('Canny Image', img_canny)

# Image dilation:  increase the thickness of edges
img_dilation = cv2.dilate(img_canny,kernel,iterations=1)
cv2.imshow('Dilation Image',img_dilation)


# Image Errosion
img_eroded = cv2.erode(img_dilation,kernel,iterations=1)
cv2.imshow('Eroded Image',img_eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()