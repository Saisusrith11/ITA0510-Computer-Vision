import cv2
import numpy as np
image = cv2.imread("C:/Users/susri/OneDrive/Desktop/COMPUTER VISION/cofeee.jpeg", cv2.IMREAD_GRAYSCALE)
if image is not None:
    kernel = np.ones((5, 5), np.uint8)
    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Original Image", image)
    cv2.imshow("Morphological Gradient", gradient)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load the image.")

    
