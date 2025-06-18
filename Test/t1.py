import cv2 
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\flower.jpg",cv2.IMREAD_COLOR)
img1=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\flower.jpg",cv2.IMREAD_GRAYSCALE)
img2=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\flower.jpg",cv2.IMREAD_UNCHANGED)
#cv2.imshow("Color image",img)
cv2.imshow("Gray image",img1)
#cv2.imshow("unchanged image", img2)
cv2.waitKey(0)
#cv2.destroyAllWindows()
#k=cv2.waitKey(0)
#if k==ord('c'):
 #   print("image is not saved")
  #  cv2.destroyAllWindows()
#elif k==ord('s'):
 #   print("image is saved ")
 #   cv2.imwrite("A:\\Apps\\anaconda\\spyder\\DIP practise\\flower1.jpg",img2)
#    cv2.destroyAllWindows()
cv2.imwrite("A:\\Apps\\anaconda\\spyder\\DIP practise\\flowercopyimwrite.jpg",img1)
cv2.destroyAllWindows()
