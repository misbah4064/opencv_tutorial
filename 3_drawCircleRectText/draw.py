import cv2
import numpy as np 
#creating an image of size 512x512
img = np.zeros((512, 512, 3), np.uint8)
#drawing a circle of radius 50 and thickness 10
cv2.circle(img,(100,100),50,(0,255,0),10)
#drawing a rectangle between starting pt(200,200) and ending pt(400,500)
cv2.rectangle(img,(200,200),(400,500),(0,0,255),1)
#drawing line between two points
cv2.line(img,(160,160),(359,29),(255,0,0),5)
#using opencv fonts to write text on the image
cv2.putText(img,"openCV",(320,100),
	cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),1)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()