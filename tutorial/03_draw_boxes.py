import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), dtype=np.uint8)
#cv.imshow('Blank Image', img)   
#img[:] = 50, 200, 0
#cv.imshow('Green Image', img)

# cv.rectangle(img, (50,50), (250, 250), (0, 0, 250), thickness=2)
# cv.imshow('Rectangle', img)

cv.rectangle(img, (50,50), (250, 250), (0, 0, 250), thickness=cv.FILLED)
#cv.imshow('Rectangle', img)

cv.circle(img, (250,250), 50, (0,255,0), thickness=2)
#cv.imshow('Circle', img)

cv.line(img, (0,0), (250,250), (255,255,255), thickness=2)
#cv.imshow('Line', img)


cv.putText(img, "This is my first text on image", (10,350), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)
cv.imshow('Text', img)

cv.waitKey(0)