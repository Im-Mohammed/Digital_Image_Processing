#Sobel Edge detection 
import cv2 
import matplotlib.pyplot as plt 
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\mumbai.jpg",cv2.IMREAD_REDUCED_COLOR_8)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#converting because opencv uses BGR as default
RGB_img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
#convert to gray
gray=cv2.cvtColor(RGB_img,cv2.COLOR_BGR2GRAY)
#remove noise
img=cv2.GaussianBlur(gray,(3,3),0)
#Convolute with sobel kernels
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)     
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) 
#plotting images
plt.imshow(sobelx)
plt.title("Sobel Edge Detection")    

