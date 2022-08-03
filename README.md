# imageprocessingwebsite
This is the source code for fully functional image processing website, made using Python with Flask Frame work, includes application of Open CV, Pillow, and Pilgram.
Deployed On AWS

This website fucntions as when the page is loaded the index.html is rendered and the user is allowed to upload the photo which he wants to process, and the
page is redirected to processing.html page where the user can choose the effect to be applied.

The backend processing is done through python-flask api netwrok,

app.py -> is the controller file,
resources.py -> is the file where the S3 configuration are made, to connect to S3 bucket,
.env -> is the environment file, where in there are place holders for S3 bucket connection,

requiremnets.txt -> contains the environment requiremnets / modules for image processing

We are using Boto3 client for S3 connection, one can use tinys3 also.

There are methods available to dumb direct into S3 bucket, so what we have tried is to post our picture into
the structure of Bucket/uploads/Test-shridhar folder

and finnaly getting the link for processed image.

We need to remeber that we need to create a presigned url for every image if we need to acess it through S3.

The prominent effects added are, removebackground of image, sketch, pencilsketch, colored Pencil sketch, squaring the image, cartoonization of image.

any development further are welcomed!

Thanking You.

