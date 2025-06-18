import cv2
import matplotlib.pyplot as plt
# load the input image
img = cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg")
# convert BGR to RGB to display using matplotlib
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Apply Gaussian blur with kernel 5*5
GausImg5 = cv2.GaussianBlur(imgRGB,(5,5),5)
# Apply Gaussian blur with kernel 15*15
GausImg15 = cv2.GaussianBlur(imgRGB,(15,15),5)
#Plot Original, Blurred images
plt.subplot(131),plt.imshow(imgRGB),plt.title('Original Image'), plt.axis('off')
plt.subplot(132),plt.imshow(GausImg5),plt.title('Gaussian Blur (k=5*5)'), plt.axis('off')
plt.subplot(133),plt.imshow(GausImg15),plt.title('Gaussian Blur (k=15*15)'), plt.axis('off')
plt.show()