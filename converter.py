"""
@author: amogh
"""

import os
from PIL import Image

def newfolderjpeg(s):
    original = 'FILEPATH TO TIFF DIRECTORY'
    a= s.split(original)
    b=a[1]
    b=b+'/'
    newpath='NEW FOLDER-PATH FOR JPEG'+b
   # print newpath
    return newpath
yourpath = 'FILEPATH TO TIFF DIRECTORY'
c=0
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        #print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print ("A jpeg file already exists for %s" % name)
            # If a jpeg is *NOT* present, create one from the tiff.
            else:
                rooto=newfolderjpeg(root)
                outfile = os.path.splitext(os.path.join(rooto, name))[0] + ".jpg"
                try:
                    #print root
                    im = Image.open(os.path.join(root, name))
                    #print "Generating jpeg for %s" % name
                    im.thumbnail(im.size)
                    im.save(outfile, "JPEG", quality=100)
                    c=c+1
                    
                except Exception as e:
                    print (e)
