import os
import sys
path = os.getcwd()
# change this for different folders
pt = '/' + sys.argv[1]

objs = os.listdir(path + pt)

a = 0
for i in objs:
    os.rename(path + pt + '/' + i, path + pt + '/' +str(a) + '.bmp')
    a += 1
