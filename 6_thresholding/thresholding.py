import cv2

img = cv2.imread('gray.jpg', 0)
ret, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

img = cv2.imread('paper.jpg', 0)
ret, thresh1 = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY)
cv2.imshow("Thank you",thresh1)
cv2.waitKey(0)
