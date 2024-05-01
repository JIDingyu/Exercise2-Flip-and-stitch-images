import numpy as np
import cv2 as cv

img=cv.imread("mi.png")
rows,cols=img.shape[:2]

img2 = np.zeros(img.shape,np.uint8)
img3 = np.zeros(img.shape,np.uint8)
img4 = np.zeros(img.shape,np.uint8)

dst = np.zeros((rows*2,cols*2,3),np.uint8)

for i in range(rows):
    for j in range(cols):
        img2[i,j] = img[i,cols-1-j]

for i in range(rows):
    for j in range(cols):
        img3[i,j] = img[rows-1-i,j]

for i in range(rows):
    for j in range(cols):
        img4[i,j] = img3[i,cols-1-j]

for i in range(rows):
    for j in range(cols):
        dst[i,j] = img[i,j]
        dst[i,j+cols] = img2[i,j]
        dst[i+rows,j]=img3[i,j]
        dst[i+rows,j+cols]=img4[i,j]

cv.imshow('img',dst)
cv.imwrite('mirror1.png',dst)