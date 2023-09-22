import cv2
import numpy as np

# Load input image
img = cv2.imread('sad64.jpg') 

# Prepare a grayscale version of the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# Detect edges in the image
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Create a color version of the edge mask
color_edges = cv2.bilateralFilter(img, 9, 250, 250) 
cartoon = cv2.bitwise_and(color_edges, color_edges, mask=edges)

# Combine input image and cartoon version
result = cv2.stylization(img, cartoon, sigma_s=150, sigma_r=0.25)

# Save output image 
cv2.imwrite('cartoon.jpg', result)
