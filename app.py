from fileinput import filename
from flask import Flask, request, render_template
import os
import boto3
import botocore
from PIL import Image
import pilgram
from config import S3_BUCKET
from removebg import remove_background
import cv2
import urllib
import io
from resources import *
import numpy as np
from grayScale import gray_scale
from sepia import convertSepia
from sketch import *
from cartoon import cartoonize
from squaresize import to_square



client = boto3.client('s3')


def create_presigned_url(bucket, object):
    try:
        url = client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket,
                'Key': object
            },
            HttpMethod='GET'
        )
    except botocore.exceptions.ClientError as e:
        return None
    return url


def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image


app = Flask(__name__)


# default access page
@app.route("/")
def main():
    return render_template('index.html')


# upload selected image and forward to processing page
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    my_bucket = get_bucket()
    my_bucket.Object(file.filename).put(
        Key="uploads/Test-shridhar/"+file.filename, Body=file)

    url2 = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file.filename)

    # file support verification
    ext = os.path.splitext(file.filename)[1]
    if (ext == ".jpg") or (ext == ".png") or (ext == ".bmp") or (ext == ".jpeg"):
        # forward to processing page
        return render_template("processing.html", image_name=url2, fileName=os.path.splitext(file.filename)[0])
    else:
        return render_template("error.html", message="The selected file is not supported"), 400


# removebg
@app.route("/removebg", methods=["POST"])
def removebg():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = remove_background(read_img)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-rembg.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-rembg.png")
    

    return render_template("processed.html", image_name=url)


# grayscale
@app.route("/grayscale", methods=["POST"])
def grayscale():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = gray_scale(read_img)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-grayscale.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-grayscale.png")

    return render_template("processed.html", image_name=url)


# sketch
@app.route("/sketch", methods=["POST"])
def sketch():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = sketchFunction(read_img)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-sketch.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-sketch.png")
    

    return render_template("processed.html", image_name=url)


# pencilsketch
@app.route("/pencilsketch", methods=["POST"])
def pencilsketch():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = pencil_sketch(read_img)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-pencilsketch.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-pencilsketch.png")

    return render_template("processed.html", image_name=url)


# Colored pencilsketch
@app.route("/coloredpencilsketch", methods=["POST"])
def colorPencilSketch():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = color_pencil_sketch(read_img)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-colorpencilsketch.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-colorpencilsketch.png")

    return render_template("processed.html", image_name=url)


# hudson
@app.route("/hudson", methods=["POST"])
def hudson():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = pilgram.hudson(Image.fromarray(read_img))

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-hudson.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-hudson.png")

    return render_template("processed.html", image_name=url)


# moon
@app.route("/moon", methods=["POST"])
def moon():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = pilgram.moon(Image.fromarray(read_img))

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-moon.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-moon.png")

    return render_template("processed.html", image_name=url)

# toaster


@app.route("/toaster", methods=["POST"])
def toaster():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = pilgram.toaster(Image.fromarray(read_img))

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-toaster.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-toaster.png")

    return render_template("processed.html", image_name=url)



# cartoonize
@app.route("/cartoon", methods=["POST"])
def cartoon():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = cartoonize(read_img)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-cartoon.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-cartoon.png")

    return render_template("processed.html", image_name=url)


# sephia
@app.route("/sephia", methods=["POST"])
def sephia():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = convertSepia(read_img)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-sepia.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-sepia.png")

    return render_template("processed.html", image_name=url)


# convert to square shape
@app.route("/square", methods=["POST"])
def square():
    filename = request.form['image']
    file = request.form['fileName']
    my_bucket = get_bucket()

    # open and process image
    read_img = url_to_image(filename)

    img = to_square(read_img)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # save and return image
    my_bucket.Object(img).put(
        Key="uploads/Test-shridhar/"+file+"-square.png", Body=img_byte_arr)

    url = create_presigned_url(
        S3_BUCKET, "uploads/Test-shridhar/"+file+"-square.png")

    return render_template("processed.html", image_name=url)



if __name__ == "__main__":
    app.run()