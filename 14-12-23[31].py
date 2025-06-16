#Implement box filter in python 
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blur=cv2.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title("Original"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title("blurred"),plt.xticks([]),plt.yticks([])
plt.show()