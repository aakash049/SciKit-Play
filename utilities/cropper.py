from PIL import Image
from PIL import ImageGrab

import time

coords = (203, 169, 846, 736)
i = 1
while True:
    img = ImageGrab.grab()
    img = img.crop(coords)
    img.save('img ' + str(i) + '.bmp')
    i += 1
    time.sleep(0.4)