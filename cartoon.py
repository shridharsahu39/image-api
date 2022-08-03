from tkinter import Image
import cv2
import numpy as np
from PIL import Image


sigma_s = 100            # range between 0 to 200
sigma_r = 0.25           # range between 0 to 1.


def cartoonize(img):
    color_cartoon = cv2.stylization(img, sigma_s=sigma_s, sigma_r=sigma_r)
    return Image.fromarray(color_cartoon)
