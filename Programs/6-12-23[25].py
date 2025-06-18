import cv2
import matplotlib.pyplot as plt 
img=cv2.imread("D:/7040/dropcol.jpeg",cv2.IMREAD_REDUCED_COLOR_4)
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
g5blur=cv2.GaussianBlur(gray,(5,5),1)
plt.subplot(221),plt.imshow(imgRGB),plt.title('Original Image'),plt.axis('off')
plt.subplot(222),plt.imshow(gray,cmap='gray'),plt.title('Grayscale Image'),plt.axis('off')
plt.subplot(223),plt.imshow(g5blur,cmap='gray'),plt.title('Kernel Size 3'),plt.axis('off')