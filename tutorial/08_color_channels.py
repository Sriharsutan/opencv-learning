import cv2 as cv

img = cv.imread('images/image1.jpg')
def rescaleFrame(frame, scale=0.2):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img, scale=0.1)
b,g,r = cv.split(img)
cv.imshow('Blue Channel', b)
cv.imshow('Green Channel', g)
cv.imshow('Red Channel', r)
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)
cv.waitKey(0)