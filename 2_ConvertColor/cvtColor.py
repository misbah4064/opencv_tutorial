import cv2

src = cv2.imread("color.jpg")
# img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# img = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
img = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
cv2.imshow("Original Image",src)
cv2.imshow("Converted Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()