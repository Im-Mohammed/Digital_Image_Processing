import cv2
img=cv2.imread("D:\\7040\\landscapecol.jpg",cv2.IMREAD_REDUCED_COLOR_4)
height=img.shape[0]
width=img.shape[1]
print("Height",height)
print("Width",width)