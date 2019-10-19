import cv2
image1 = cv2.imread('nightpic.jpg')
image2 = cv2.imread('nightpic.jpg')
resized_image1 = cv2.resize(image1, (1000, 1000))
resized_image2 = cv2.resize(image2, (1000, 1000)) 
gray_image1 = cv2.cvtColor(resized_image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(resized_image2, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image1.png',gray_image1)
cv2.imwrite('gray_image2.png',gray_image2)

cv2.imshow('color_image1',resized_image1)
cv2.imshow('gray_image1',gray_image1) 
cv2.imshow('color_image2',resized_image2)
cv2.imshow('gray_image2',gray_image2)

cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
