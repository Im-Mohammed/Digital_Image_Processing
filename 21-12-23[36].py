import cv2
import matplotlib.pyplot as plt 
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sudoku.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img=cv2.medianBlur(img,5)
#global thresholding
ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ADaptive threshloding
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) 
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#plotting the images using matplotlib
titles=["Orginal",'Global Thresholding','Adaptive Mean Thresholding',"Adaptive Gaussian thresholding"]
images=[img,th1,th2,th3] 
plt.figure(figsize=(10,10))
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray'),plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()           