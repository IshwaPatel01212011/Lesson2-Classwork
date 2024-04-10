import cv2
import os 
import numpy as np

bg = cv2.imread("Lesson 2/images/bg.jpg")
dimond = cv2.imread("Lesson 2/images/dimond.jpg")
star = cv2.imread("Lesson 2/images/star.jpg")
tiger = cv2.imread("Lesson 2/images/tiger.png")

# adding the images
storing = cv2.addWeighted(star, 0.4, dimond, 0.6, 1)
cv2.imshow("add",storing)
cv2.waitKey(0)

# subtrating the images
subtract = cv2.subtract(star, dimond)
cv2.imshow("subtract",subtract)
cv2.waitKey(0)

# resizing the images
resize = cv2.resize(dimond, (400,170))
print(os.getcwd())
path = "/Users/ishwa/Documents/Jetlearn/OpenCV and Face Identification/Lesson 2"
os.chdir(path)
cv2.imwrite("dimond.jpg",resize)

# eroding the image
kernel = np.ones((7,7),np.uint8)
erode = cv2.erode(bg,kernel)
cv2.imshow("erosion",erode)
cv2.waitKey(0)

#BLURRING THE IMAGE
# common blur
common = cv2.GaussianBlur(bg,(3,3),0,0)
cv2.imshow("common blur",common)
cv2.waitKey(0)

#median blur 
median = cv2.medianBlur(tiger,5)
cv2.imshow("median blur",median)
cv2.waitKey(0)

#bilateral blur 
bilateral = cv2.bilateralFilter(bg,7,80,82)
cv2.imshow("bilateral blur",bilateral)
cv2.waitKey(0)

# borders
border = cv2.copyMakeBorder(tiger,25,25,50,50,cv2.BORDER_REFLECT)
cv2.imshow("drawing the border",border)
cv2.waitKey(0)