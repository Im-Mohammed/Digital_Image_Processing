import cv2
import numpy as np
# load the image and convert to grayscale
image = cv2.imread("A:\\Apps\\anaconda\\spyder\\DIP practise\\sunflower.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Compute the Discrete Fourier Transform of the image
fourier = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
# calculate the magnitude of the Fourier Transform
magnitude = 20*np.log(cv2.magnitude(fourier[:,:,0],fourier[:,:,1]))
# Scale the magnitude for display
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX,
cv2.CV_8UC1)
#Inverse DFT
idft = cv2.idft(fourier)
# calculate the magnitude of the Inverse Fourier Transform
imag = 20*np.log(cv2.magnitude(idft[:,:,0],idft[:,:,1]))
# Scale the magnitude for display
imagnorm = cv2.normalize(imag, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
# Display the magnitude of the Fourier Transform
cv2.imshow("Original Image",gray)
cv2.imshow('Fourier Transform', magnitude)
cv2.imshow('Magnitude Spectrum', imagnorm)
cv2.waitKey(0)
cv2.destroyAllWindows()
