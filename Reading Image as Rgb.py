import cv2
import matplotlib.pyplot as plt
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\3circle_1.jpg")
gry=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
B,G,R=cv2.split(gry)
plt.subplot(221),plt.imshow(img),plt.title("Original Imgae"),plt.axis('off')
plt.subplot(222),plt.imshow(R),plt.title('Red COlor'),plt.axis("off")
plt.subplot(223),plt.imshow(G),plt.title("Green Color"),plt.axis('off')
plt.subplot(224),plt.imshow(B),plt.title("Blue Color"),plt.axis("off")
gr1=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg")
rgb=cv2.cvtColor(gr1,cv2.COLOR_BGR2RGB)
cv2.imshow("RGb Image",rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()