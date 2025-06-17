import cv2
import matplotlib.pyplot as plt
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\flower1.jpg",cv2.IMREAD_REDUCED_COLOR_4)
#1 program
#convert into rgb
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Original Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#2 program splitting rgb images
#cv2.imshow("Original Image",img)
r,g,b=cv2.split(img)
#cv2.imshow("Red Color",r)
#cv2.imshow("Blue Color",b)
#cv2.imshow("green Color",g)
#or
#plt.subplot(221),plt.imshow(img),plt.title("Original"),plt.axis('off')
#plt.subplot(222),plt.imshow(r,cmap="gray"),plt.title("Red Channel"),plt.axis('off')
#plt.subplot(223),plt.imshow(g,cmap="gray"),plt.title("gree Channel"),plt.axis('off')
#plt.subplot(224),plt.imshow(b,cmap="gray"),plt.title("blue Channel"),plt.axis('off')
#cv2.waitKey(0)
#cv2.destroyAllWindows()