import cv2
#reading images as grey scale
img=cv2.imread('A:\\Apps\\anaconda\\spyder\\DIP practise\\flower.jpg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()