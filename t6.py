import cv2
import matplotlib.pyplot as plt
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg")
imgrgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur1=cv2.GaussianBlur(imgrgb,(7,7), 1)
blur2=cv2.blur(imgrgb,(10,10))
plt.subplot(221),plt.imshow(imgrgb),plt.title("Original"),plt.axis("Off")
plt.subplot(222),plt.imshow(gray,cmap='gray'),plt.title("gray Image"),plt.axis('off')
plt.subplot(223),plt.imshow(blur1),plt.title("Blurred Image"),plt.axis('off')
plt.subplot(224),plt.imshow(blur2),plt.title("Blurred Image 2"),plt.axis('off')