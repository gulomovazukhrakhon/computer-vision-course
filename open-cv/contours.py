import cv2 as cv
import numpy as np

# Reading Photos
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours')

cv.drawContours(blank, contours, -1, (100, 100, 0), 1)
cv.imshow('Contours Drawn', blank)

cv.drawContours(canny, contours, -1, (205, 0, 100), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
