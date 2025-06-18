#Convert to colored image to binary 
import cv2 
import matplotlib.pyplot as plt
image=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg")
cv2.imshow("Original",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap="gray")
(thresh,binary_image)=cv2.threshold(gray_image,175,255,cv2.THRESH_BINARY)
plt.imshow(binary_image,cmap='gray')