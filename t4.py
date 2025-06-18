#converting to gray scale image
import cv2 
img=cv2.imread('A:\\Apps\\anaconda\\spyder\\DIP practise\\flower.jpg',0)
i1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",i1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#2nd Program
#dim=img.shape
#print(dim)
#h=img.shape[0]
#w=img.shape[1]
#ch=img.shape[2]
#print("height",h)
##print("channels",ch)
#for i in range(h):
 #   for j in range(w):
  #      img[i,j]=sum(img[i,j])*0.33
#cv2.imshow("Gray image",img)