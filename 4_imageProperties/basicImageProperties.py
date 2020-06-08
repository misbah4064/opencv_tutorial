import  cv2

img = cv2.imread( 'color.jpg' )
cv2.imshow("original",img)

# pixel = img[100,100]
# print(pixel)

# blue_pixel = img [ 100,100,0 ]
# print ( blue_pixel )


# img [ 100, 100 ] = [ 255 , 255 , 255 ]
# print(img[100,100])

# print (img.shape)
# height,width,channels = img.shape
# print(height,width,channels)


# region_of_interest = img[94:372,47:276 ]
# cv2.imshow ('ROI',region_of_interest )
# cv2.waitKey ( 0 )


blue_channel  =  img [:, :, 0]
green_channel  =  img [:, :, 1]
red_channel  =  img [:, :, 2]
cv2.imshow('blue_channel',blue_channel)
cv2.imshow('green_channel',green_channel)
cv2.imshow('red_channel',red_channel)
cv2 . waitKey ( 0 )