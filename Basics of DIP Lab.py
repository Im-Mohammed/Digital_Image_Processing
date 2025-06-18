import cv2
print(cv2.__version__)
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg")
img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Image Test", img1)
cv2.waitKey()
cv2.destroyAllWindows()