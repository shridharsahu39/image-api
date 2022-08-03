import rembg
from rembg import remove
from PIL import Image


def remove_background(img):
    img = remove(img, alpha_matting=True, alpha_matting_foreground_threshold =240, alpha_matting_background_threshold =10, alpha_matting_erode_size=5)
    return Image.fromarray(img)
