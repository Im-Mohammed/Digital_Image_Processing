import cv2
img=cv2.imread("D:\\7040\\landscapecol.jpg",cv2.IMREAD_REDUCED_COLOR_4)
dimensions=img.shape
print(dimensions)
height=img.shape[0]
width=img.shape[1]
channels=img.shape[2]
print("Image Dimensions",dimensions)
print("Height",height)
print("Width",width)
print("Number of channels ",channels)
for i in range(height):
    for j in range(width):
        img[i,j]=sum(img[i,j])/3
        
cv2.imshow("Converted img ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()