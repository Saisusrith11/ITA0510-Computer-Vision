




import cv2
import numpy as np
image = cv2.imread("C:/Users/susri/OneDrive/Desktop/COMPUTER VISION/draw village.jpg")
height, width = image.shape[:2]
center = (width // 2, height // 2)
angle = 45 
clockwise_rotation_matrix = cv2.getRotationMatrix2D(center, -angle, 1.0)
rotated_clockwise = cv2.warpAffine(image, clockwise_rotation_matrix, (width, height))
counterclockwise_rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_counterclockwise = cv2.warpAffine(image, counterclockwise_rotation_matrix, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Clockwise Rotation', rotated_clockwise)
cv2.imshow('Counterclockwise Rotation', rotated_counterclockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
