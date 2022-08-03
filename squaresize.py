import numpy as np
from PIL import Image


def to_square(img):
    # get bigger side of the image
    s = max(img.shape[0:2])
    # create a black background
    img_square = np.zeros((s, s, 3), np.uint8)
    # get the centering position
    ax, ay = (s - img.shape[1])//2, (s - img.shape[0])//2
    # place the image to the center of the background
    img_square[ay:img.shape[0]+ay, ax:ax+img.shape[1]] = img
    return Image.fromarray(img_square)
