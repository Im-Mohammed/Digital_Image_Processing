import cv2
#Reading an Image multiple images
#img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\flower1.jpg",cv2.IMREAD_REDUCED_COLOR_4)
#img1=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg",-1)
#cv2.imshow("Original Image",img)cc#v2.imshow("Second Image",img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#Writing an Image
img2=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg",0)
status=cv2.imwrite("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflowergray.jpg",img2)
cv2.imshow("Gray image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Image is written to a file",status)
#Storing An Image
img3=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg")
gry=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg",0)
cv2.imshow("Image to be Saved",img3)
k=cv2.waitKey(0)
if k==ord('s'):
    cv2.imwrite("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflowergray.jpg",img3)
    print("color image is Saved")
    cv2.destroyAllWindows()
elif k==ord('g'):
    cv2.imwrite("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\sunflower.jpg",gry)
    print("gray Image is saved")
    cv2.destroyAllWindows()