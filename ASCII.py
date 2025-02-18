from PIL import Image
import numpy as np
import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments! include the path to an image")
else:
    path = sys.argv[1]

size = (100,100)
img = Image.open(path)
#img = img.resize(size)

img_array = np.array(img.convert("RGB"))

pixel_ascii_map = " .,:irs?@9B&#"
#pixel_ascii_map =  "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

for x in range(len(img_array)):
    for y in range(len(img_array[x])):
        r, g, b = img_array[x][y]
        brightness = int((r + g + b) / 3)
        ascii = int((brightness * len(pixel_ascii_map)) / 255)
        print(pixel_ascii_map[ascii], end="")


