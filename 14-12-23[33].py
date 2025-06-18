#Erosion
import cv2
import numpy as np 
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg",0)
#Define Structuring element 
kernel=np.ones((5,5),np.uint8)
#perform Erosion
Erosion=cv2.erode(img,kernel,iterations =1)
#display results
cv2.imshow("Original",img)
cv2.imshow("Erosion ",Erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()