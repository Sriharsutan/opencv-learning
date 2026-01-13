import cv2 as cv
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')  # Or 'Qt5Agg', 'GTK3Agg', etc., depending on your system

img = cv.imread('images/image1.jpg')

#Grayscale histogram
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Grayscale Image', gray)
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)