import cv2
import numpy as np
from PIL import Image


def convertSepia(image):
    """
    Optimization on the sepia filter using cv2 
    """

    # Load the image as an array so cv knows how to work with it
    img = np.array(image)

    # Apply a transformation where we multiply each pixel rgb
    # with the matrix for the sepia

    filt = cv2.transform(img, np.matrix([[0.393, 0.769, 0.189],
                                         [0.349, 0.686, 0.168],
                                         [0.272, 0.534, 0.131]
                                         ]))

    # Check wich entries have a value greather than 255 and set it to 255
    filt[np.where(filt > 255)] = 255

    # Create an image from the array
    return Image.fromarray(filt)
