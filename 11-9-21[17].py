import cv2
import matplotlib.pyplot as plt 
img=cv2.imread("D:\\7040\\3circle.jpg")
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.subplot(221),plt.imshow(rgb),plt.title("Original Image "),plt.axis("off")
r,g,b=cv2.split(rgb)
plt.subplot(222),plt.imshow(r,cmap='gray'),plt.title("Red Channel"),plt.axis("off")
plt.subplot(223),plt.imshow(g),plt.title("Green channel "),plt.axis("off")
plt.subplot(224),plt.imshow(b),plt.title("Blue channel "),plt.axis("off")