#export PYTHONPATH="/usr/local/opencv-2.4.9/lib/python2.7/site-packages/"


import os
import sys
import glob
import cv2
import numpy as np
import argparse

from timeit import default_timer as timer

''' 
    Usage :
    ./db_indexing.py -d "database_name"
    
    Example :
    ./db_indexing.py -d "base1"
'''

######## Program parameters

parser = argparse.ArgumentParser()

## Database name
parser.add_argument("-d", "--database", dest="db_name",
                    help="input image database", metavar="STRING", default="None")

args = parser.parse_args()

## Set paths
img_dir="/share/esir3/VO/Images/" + args.db_name + "/"
imagesNameList = glob.glob(img_dir+"*.jpg")
output_dir="./results/" + args.db_name

if not os.path.exists(img_dir):
    print "The directory containing images: "+img_dir+" is not found -- EXIT\n"
    sys.exit(1)









