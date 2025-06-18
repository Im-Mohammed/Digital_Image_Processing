#Implementing averaging and gaussian filter
import cv2
#import numpy as np 
import matplotlib.pyplot as plt 
image1=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg")
cv2.imshow("Original Image",image1)
cv2.waitKey(0)
gaussian1=cv2.GaussianBlur(image1,(7,7),0)
cv2.imshow("Gaussian Blurring", gaussian1)
cv2.waitKey(0)
image1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
avg=cv2.blur(image1,(10,10))
plt.imshow(avg)
cv2.waitKey(0)
cv2.destroyAllWindows()