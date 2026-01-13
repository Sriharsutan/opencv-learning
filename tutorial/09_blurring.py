import cv2 as cv
import numpy as np

img = cv.imread('images/image1.jpg')
def rescaleFrame(frame, scale=0.2):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img, scale=0.1)

# Average blurring
average = cv.blur(img, (3,3))
cv.imshow('Average Blurring', average)

# Gaussian Blurring
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blurring', gauss)   

# Median Blurring
median = cv.medianBlur(img, 3)
cv.imshow('Median Blurring', median)    

# Bilateral Blurring
bilateral = cv.bilateralFilter(img, 5, 15, 15)  
cv.imshow('Bilateral Blurring', bilateral)
cv.waitKey(0)