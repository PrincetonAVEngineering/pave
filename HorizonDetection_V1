# PAVE SOLUTION: Horizon Detection
# Based on Horizon Detection Using Basic Image Processing from
# Based on: https://github.com/sallamander/horizon-detection/blob/master/detect_horizons.py

import cv2 # OpenCV package
import numpy as np # Numerical python

# The following two are for selecting a file in your directory
from tkinter import filedialog 
from tkinter import *

# Used to draw plots and the associated horizon line
import matplotlib.pyplot as plt

def find_horizon(image_grayscale):
    # Ensures that the input is a 2D image (.ndim returns dimensions)
    msg = ('image_grayscaled should be a grayscale, 2D image of shape (height, width).')
    assert image_grayscale.ndim == 2, msg

    # Blurs image to reduce noise (data points that may interfere with segmentation)
    image_blurred = cv2.blur(image_grayscale, (5,5))
    # cv2.imshow("IMGBLUR", image_blurred)

    # Creates a threshold for the image (uses Binary and Otsu thresholds)
    _, image_threshold = cv2.threshold(
        image_blurred, thresh = 0, maxval = 1,
        type = cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    # Brings the threshold between 0 and 1 for actual use
    image_threshold = image_threshold - 1

    # Fills in gaps in the image 
    image_closed = cv2.morphologyEx(image_threshold, cv2.MORPH_CLOSE,
                                    kernel=np.ones((9, 9), np.uint8))
    
    # cv2.imshow("closed", image_closed)

    # X coordinates are first and last lengthwise pixels
    horizon_x1 = 0
    horizon_x2 = image_grayscale.shape[1] - 1

    # Y-coordinates for the horizon line
    horizon_y1 = max(np.where(image_closed[:, horizon_x1] == 0)[0])
    horizon_y2 = max(np.where(image_closed[:, horizon_x2] == 0)[0])

    return horizon_x1, horizon_x2, horizon_y1, horizon_y2
    
if __name__ == "__main__":
    # Destroy root window (used for selecting files)
    root = Tk()
    root.withdraw()

    # Select file name and cleanse it
    path = filedialog.askopenfile().name
    path = path.replace("/", "//")

    # Sets plot to draw horizon line
    fig, axes = plt.subplots(1, 2)

    # Pass image to be read
    image = cv2.imread(path)

    # Converts the image to grayscale
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #REMOVE LINE
    
    #cv2.imshow("gray", image_grayscale)

    horizon_x1, horizon_x2, horizon_y1, horizon_y2 = (
        find_horizon(image_grayscale)
    )

    # Plots the original image
    axes[0].imshow(image)
    axes[0].axis('off')
    axes[0].set_title('Original Image')

    # Plots the gray-scaled image w/ horizon line
    axes[1].imshow(image_grayscale, cmap='gray')
    axes[1].axis('off')
    axes[1].plot(
        (horizon_x1, horizon_x2), (horizon_y1, horizon_y2),
        color='r', linewidth='2'
    )

    # Shows the plot
    plt.show()
    plt.close()

    cv2.imshow("IMAGE", image_grayscale)
    cv2.waitKey(0)