import cv2 as cv
import numpy as np

img = cv.imread('images/image1.jpg')
def rescaleFrame(frame, scale=0.2):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img, scale=0.1)

#Gray Scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

#Blurring the image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blurred Image', blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated Image', dilated)

#Eroding the image
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded Image', eroded)

#Crop the image
cropped = img[50:200, 200:400]
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)