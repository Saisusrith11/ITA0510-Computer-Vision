import cv2
import numpy as np
image = cv2.imread ("C:/Users/susri/Downloads/Girl with a Cat.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
grad_x = cv2.Scharr(blurred, cv2.CV_64F, 1, 0)
grad_y = cv2.Scharr(blurred, cv2.CV_64F, 0, 1)
gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
gradient_magnitude = np.uint8(gradient_magnitude)
sharpened = cv2.addWeighted(gray, 1.5, gradient_magnitude, -0.5, 0)
cv2.imshow('Original Image', gray)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()


