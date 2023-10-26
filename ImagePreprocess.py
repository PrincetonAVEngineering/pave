# IMAGE PREPROCESSING
# Princeton Autonomous Vehicles Engineering
# October 15, 2023

import cv2
import numpy as np

def imagePreprocess(frame):
    # Defines the kernel
    kerSize = 15
    # Define top boundary and lower boundary (y-values)
    topBound = 50
    lowBound = 430
    # Define thresholding blocksize
    blocksize = 11

    # Crops the image
    frame = frame[topBound:lowBound]

    # Converts image to grayscale
    modImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blurs the image
    modImg = cv2.GaussianBlur(modImg, (kerSize,kerSize), 0)

    # Adaptive thresholding: potential counter to lighting/reflections?
    modImg = cv2.adaptiveThreshold(modImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, blocksize, 2)

    return modImg