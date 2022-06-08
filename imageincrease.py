from PIL import Image

size = 7680, 7680
im = Image.open("output/2022-06-08-example-prompts/girl-with-blonde-hair-by-picasso.jpg")
im_resized = im.resize(size, Image.ANTIALIAS)
im_resized.save("sea.jpg", dpi=(1200, 1200))
