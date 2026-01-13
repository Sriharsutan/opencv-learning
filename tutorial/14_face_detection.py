import cv2 as cv

img = cv.imread('images/dhoni.jpeg')
cv.imshow('Original Image', img)

face_cascade = cv.CascadeClassifier('haar_face.xml')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)