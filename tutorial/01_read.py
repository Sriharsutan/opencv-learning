import cv2 as cv

# im1 = cv.imread('images/image1.jpg')
# cv.imshow('Image 1', im1)
# cv.waitKey(0)

capture = cv.VideoCapture('videos/video1.mp4')
while True:
    isTrue,frame = capture.read()
    if not isTrue:
        break
    cv.imshow('Video Frame', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break  

capture.release()
cv.destroyAllWindows()