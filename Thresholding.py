import cv2
import matplotlib.pyplot as plt
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sudoku.png")
th1=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
#adaptive Thresholding
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV, 15,2)
plt.subplot(221),plt.imshow(img),plt.title("Original Image"),plt.axis('off')
plt.subplot(222),plt.imshow(th1),plt.title("Global THresholding"),plt.axis('off')
plt.subplot(223),plt.imshow(th2),plt.title("Adaptive THresholding"),plt.axis('off')
plt.subplot(224),plt.imshow(th3),plt.title("Adaptive THresholding Mean"),plt.axis('off')