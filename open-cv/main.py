import cv2

# Reading Photos
img = cv2.imread('Photos/cat_large.jpg')

cv2.imshow('Cat', img)

# Reading Videos
capture = cv2.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

cv2.waitKey(0)
