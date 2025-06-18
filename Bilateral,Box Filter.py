#Bilateral Filter
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg")
bf=cv2.bilateralFilter(img,5, 75,75)
b0x=cv2.blur(img,(15,15))
bf1=cv2.bilateralFilter(img,10,100,100)
cv2.imshow("Original Image", img)
cv2.imshow("Bilateral Filter",bf)
cv2.imshow("Box Filter",b0x)
cv2.waitKey()
cv2.destroyAllWindows()
