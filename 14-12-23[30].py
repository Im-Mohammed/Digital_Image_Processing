#implement bilateral blur in python 
import cv2
import matplotlib.pyplot as plt 
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\landscapecol1.jpg")
imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
billmg5=cv2.bilateralFilter(imgRGB,5,75,75)
billmg15=cv2.bilateralFilter(imgRGB,15,100,100)
plt.subplot(131),plt.imshow(imgRGB),plt.title("Original Image"),plt.axis("off")
plt.subplot(132),plt.imshow(billmg5),plt.title("Bilateral Blur d=5"),plt.axis("off")
plt.subplot(133),plt.imshow(billmg15),plt.title("Bilateral Blur d=15"),plt.axis("off")