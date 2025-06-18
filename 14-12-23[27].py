import cv2
#import numpy as np 
import matplotlib.pyplot as plt 
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg")
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.imshow(img)
img=cv2.blur(img,(10,10))
plt.imshow(img)