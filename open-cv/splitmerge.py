import cv2 as cv
import numpy as np

# Reading Photos
img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# Blank Image
blank = np.zeros(img.shape[:2], dtype='uint8')

# Splitting color channels
b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merging color channels
merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)



cv.waitKey(0)
