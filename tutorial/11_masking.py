import cv2 as cv
import numpy as np

img = cv.imread('images/image1.jpg')
def rescaleFrame(frame, scale=0.2):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img, scale=0.1)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Masked Image', masked)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
masked_rectangle = cv.bitwise_and(img, img, mask=rectangle)
cv.imshow('Masked Rectangle', masked_rectangle)


cv.waitKey(0)