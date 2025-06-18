import cv2
import matplotlib.pyplot as plt
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\flower1.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.subplot(221),plt.imshow(img),plt.title("Color Image"),plt.axis('off')
plt.subplot(222),plt.imshow(gray),plt.title("Gray Image"),plt.axis('off')
#Averaging method
dim=img.shape
h=img.shape[0]
w=img.shape[1]
ch=img.shape[2]
print("Dimensions: ",dim)
print("Height: ",h)
print("Width: ",w)
print("Channels: ",ch)
for i in range(h):
    for j in range(w):
        img[i,j]=sum(img[i,j])*0.33
cv2.imshow("Gray Scale Image: ",img)
cv2.waitKey()
cv2.destroyAllWindows()