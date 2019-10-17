import cv2
image = cv2.imread('nightpic.jpg')
resized_image = cv2.resize(image, (1000, 1000)) 
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png',gray_image)
cv2.imshow('color_image',resized_image)
cv2.imshow('gray_image',gray_image) 
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
