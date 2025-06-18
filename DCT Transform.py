import cv2 
import numpy as np
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#dct
dctimg=cv2.dct(np.float32(gray),cv2.DCT_INVERSE)
#invdct
idct=cv2.idct(dctimg)
idc=np.uint8(idct)
cv2.imshow("Origianl",img)
cv2.imshow("Gray Image",gray)
cv2.imshow(" Dct Image",dctimg)
cv2.imshow("Indct Image",idct)
cv2.waitKey()
cv2.destroyAllWindows()