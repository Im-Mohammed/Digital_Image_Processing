import cv2
import numpy as np
# load the image and convert to grayscale
image = cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Compute the Discrete Cosine Transform of the image
dctimg = cv2.dct(np.float32(gray), cv2.DCT_INVERSE)
#Inverse DCT
idctimg = cv2.idct(dctimg)
# convert to uint8
idct = np.uint8(idctimg)
#DIP LAB PROGRAMS - Prepared by Dr Diana Moses, CSE, MCET, Pg No —54
# Display the results
cv2.imshow("Original Image",gray)
cv2.imshow('Cosine Transform', dctimg)
cv2.imshow('Inverse Cosine Transform', idct)
cv2.waitKey(0)
cv2.destroyAllWindows()