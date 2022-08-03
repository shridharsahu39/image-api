import cv2
import PIL
from PIL import Image


def sketchFunction(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    img = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    return Image.fromarray(img)


def pencil_sketch(img):
    # PENCIL SKETCH  ##########
    # convert the image to gray_sketch and color_sketch
    sigma_s = 150            # range between 0 to 200
    sigma_r = 0.3            # range between 0 to 1.
    shade_factor = 0.08    # range between 0 to 0.1
    gr_sketch, cl_sketch = cv2.pencilSketch(img,
                                            sigma_s=sigma_s,
                                            sigma_r=sigma_r,
                                            shade_factor=shade_factor)
    return Image.fromarray(gr_sketch)


def color_pencil_sketch(img):
    # PENCIL SKETCH  ##########
    # convert the image to gray_sketch and color_sketch
    sigma_s = 150            # range between 0 to 200
    sigma_r = 0.1            # range between 0 to 1.
    shade_factor = 0.08   # range between 0 to 0.1
    gr_sketch, cl_sketch = cv2.pencilSketch(img,
                                            sigma_s=sigma_s,
                                            sigma_r=sigma_r,
                                            shade_factor=shade_factor)
    return Image.fromarray(cl_sketch)
