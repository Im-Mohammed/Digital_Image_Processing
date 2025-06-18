import cv2
img=cv2.imread("D:\\7040\\landscapecol.jpg",cv2.IMREAD_REDUCED_COLOR_4)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Grayscale image ",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()