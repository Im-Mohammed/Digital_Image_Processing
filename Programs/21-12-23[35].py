  import cv2 
from matplotlib import pyplot as plt 
#loading images 
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\mumbai.jpg")
#converting to gray scale 
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#remove Noise 
img=cv2.GaussianBlur(gray,(3,3),0)
#convolute with proper kernels 
laplacian=cv2.Laplacian(img,cv2.CV_64F)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)     
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) 
plt.subplot(2,2,1),plt.imshow(img,cmap="gray"),plt.title("Original"),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap="gray"),plt.title("laplacian"),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap="gray"),plt.title("SobleX"),plt.xticks([]),plt.yticks([])
