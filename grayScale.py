from PIL  import Image,ImageOps,ImageEnhance

def gray_scale(img):
    gray = ImageOps.grayscale(Image.fromarray(img))
    enhancer = ImageEnhance.Contrast(gray)
    im_output = enhancer.enhance(1.2)
    enhancer2 = ImageEnhance.Brightness(im_output)
    img = enhancer2.enhance(1.1)
    return img
