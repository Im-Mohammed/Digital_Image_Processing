#dilation
import cv2
import numpy as np 
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg",0)
#Define Structuring element 
kernel=np.ones((5,5),np.uint8)
#perform dilation 
Erosion=cv2.dilate(img,kernel,iterations =1)
#display results
cv2.imshow("Original",img)
cv2.imshow("Dilate ",Erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()