import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg")
k=np.ones((5,5))
ero=cv2.erode(img,k,1)
dil=cv2.dilate(img,k,5)
cv2.imshow("Original Image",img)
cv2.imshow("Erosion",ero)
cv2.imshow("Dilation",dil)
cv2.waitKey()
cv2.destroyAllWindows()