import cv2
import matplotlib.pyplot as plt
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\jerry.png",-1)
ret,th1=cv2.threshold(img,120, 255, cv2.THRESH_BINARY)
#imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Bianry Image",th1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(th1)
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,th1=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
#plt.subplot(331),plt.imshow(imgrgb),plt.title("Original"),plt.axis('off')
#plt.subplot(332),plt.imshow(gray,cmap='gray'),plt.title("Gray Image"),plt.axis('off')
#plt.subplot(333),plt.imshow(th1,cmap='gray'),plt.title("Binary Image"),plt.axis('off')
#2method
#ret,th2=cv2.threshold(gray,120,255,cv2.THRESH_BINARY_INV)
#et,th3=cv2.threshold(gray,120,255,cv2.THRESH_TRUNC)
#ret,th4=cv2.threshold(gray,120,255,cv2.THRESH_TOZERO)
#et,th5=cv2.threshold(gray,120,255,cv2.THRESH_TOZERO_INV)
#plt.subplot(334),plt.imshow(th2,cmap='gray'),plt.title("Binary Image Inv"),plt.axis('off')
#3plt.subplot(335),plt.imshow(th3,cmap='gray'),plt.title("Trunc Image"),plt.axis('off')
#plt.subplot(336),plt.imshow(th4,cmap='gray'),plt.title("ToZero Image"),plt.axis('off')