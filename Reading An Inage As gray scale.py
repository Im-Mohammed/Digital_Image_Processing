import cv2
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg",0)
cv2.imshow('Gray Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#2 Method to rread as gray 
gy=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\flower1.jpg",cv2.IMREAD_REDUCED_GRAYSCALE_4)
cv2.imshow("Gray Image",gy)
cv2.waitKey(0)
cv2.destroyAllWindows()
