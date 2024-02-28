import cv2 as cv

# variable
RED = 255
GREEN = 255
BLUE = 255
ALPHA = 255

Image = cv.imread("1.png", cv.IMREAD_UNCHANGED)

trans_mask = Image[:, :, 3] == 0

Image[trans_mask] = [BLUE, GREEN, RED, ALPHA]
print(Image.shape)

resized = cv.resize(Image, None, fx=0.1, fy=0.1)
cv.imshow('windows', resized)
cv.waitKey(0)