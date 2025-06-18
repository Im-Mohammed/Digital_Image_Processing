import cv2
import numpy as np 
img=cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP lab preparation\\flower1.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#dft
df=cv2.dft(np.float32(gray),cv2.DFT_COMPLEX_OUTPUT)
#idft
idft1=cv2.idft(df)
mag=20*np.log(cv2.magnitude(df[:,:,0],df[:,:,1]))
norm=cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)
cv2.imshow("Original Image",img)
cv2.imshow("Gray ",gray)
cv2.imshow("DFT",df)
cv2.imshow("IDFT",norm)
cv2.waitKey()
cv2.destroyAllWindows()