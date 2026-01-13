import cv2 as cv

img = cv.imread('images/image1.jpg')
def rescaleFrame(frame, scale=0.2):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img, scale=0.1)

cv.imshow('BGR Image', img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV Image', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB Image', lab)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)
cv.waitKey(0)