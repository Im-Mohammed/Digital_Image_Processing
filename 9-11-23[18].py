#GRAYSCALE METHOD 1 
import cv2
gray=cv2.imread("D:\\7040\\londoncol.jpg",cv2.IMREAD_REDUCED_GRAYSCALE_4)
cv2.imshow("Gray Scale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()