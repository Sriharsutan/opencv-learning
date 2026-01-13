import cv2 as cv

img = cv.imread('images/image1.jpg')
def rescaleFrame(frame, scale=0.2):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img, scale=0.1)

#Canny Edge Detection
edges = cv.Canny(img, 100, 200)
cv.imshow('Canny Edges', edges)


#Laplacian Edge Detection
laplacian = cv.Laplacian(img, cv.CV_64F)
cv.imshow('Laplacian Edges', laplacian)

#Sobel Edge Detection
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)
cv.imshow('Sobel X Edges', sobelx)
cv.imshow('Sobel Y Edges', sobely)

sobelxy = cv.Sobel(img, cv.CV_64F, 1, 1)
cv.imshow('Sobel XY Edges', sobelxy)

cv.waitKey(0)