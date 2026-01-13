import cv2 as cv

def rescaleFrame(frame, scale=0.6):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# capture = cv.VideoCapture('videos/video2.mp4')
# while True:
#     isTrue, frame = capture.read()
#     if not isTrue:
#         break

#     frame_rescaled = rescaleFrame(frame, scale=0.2)

#     #cv.imshow('Original Video Frame', frame)
#     cv.imshow('Rescaled Video Frame', frame_rescaled)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

img = cv.imread('images/image1.jpg')
resized_image = rescaleFrame(img, scale=0.2)
cv.imshow('Rescaled Image', resized_image)
cv.waitKey(0)
cv.destroyAllWindows()