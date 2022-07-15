from PIL import Image
from os import listdir
from os.path import isfile, join

size = 7680, 7680
output = 'output/'
dirName = '2022-06-10-example-prompts'
myPath = output + dirName
files = [f for f in listdir(myPath) if isfile(join(myPath, f))]

for file in files:
    im = Image.open(join(myPath, file))
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save(f"increased/{file}", dpi=(1920, 1920))

