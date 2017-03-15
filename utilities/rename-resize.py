import os
import sys
from PIL import Image

path = os.getcwd()
# change this for different folders
pt = '/' + sys.argv[1]

objs = os.listdir(path + pt)
w = 300

a = 0
for i in objs:
	if (i.endswith('.bmp')):
		img = Image.open(path + pt + '/' + i)
		widthPercent = (w / float(img.size[0]))
		height = int(float(img.size[1]) * widthPercent)
		img = img.resize((w, height), Image.BILINEAR)
		img.save(path + pt + '/' + str(a) + '.bmp')
		a += 1