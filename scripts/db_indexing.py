#export PYTHONPATH='/usr/local/opencv-2.4.9/lib/python2.7/site-packages/'

import os
import sys
import glob
import cv2 as cv
import numpy as np
import argparse

from timeit import default_timer as timer

''' 
    Usage :
    ./db_indexing.py -d 'database_name'
    
    Example :
    ./db_indexing.py -d 'base1'
'''

######## Program parameters

parser = argparse.ArgumentParser()

## Database name
parser.add_argument('-d', '--database', dest='db_name',
                    help='input image database', metavar='STRING', default='None')

args = parser.parse_args()

## Set paths
img_dir='./Images/' + args.db_name + '/'
imagesNameList = glob.glob(img_dir+'*.jpg')
output_dir='./output/' + args.db_name

if not os.path.exists(img_dir):
    print ('The directory containing images: '+img_dir+' is not found -- EXIT\n')
    sys.exit(1)

# Read img
img_list=[cv.imread(f) for f in imagesNameList]


# Create descriptors database
dbdesc=np.array([],dtype=np.float32)
gray_list= [cv.cvtColor(img,cv.COLOR_BGR2GRAY) for img in img_list]

sift = cv.xfeatures2d.SIFT_create()
start = timer()
for i in range(0,len(gray_list)) :
    kp, des = sift.detectAndCompute(gray_list[i],None)
    dbdesc=np.concatenate((dbdesc,des[0]))
    print(str(len(des[0]))+' descriptors for '+str(imagesNameList[i]))

#stats
end = timer()
print ('Descriptors generating time: ' + str(end - start)+' seconds')
print(str(len(dbdesc))+' descriptors for this database')
print('Mean of '+str(np.round(len(dbdesc)/len(gray_list)))+' descriptors per image')
np.save(output_dir+'_dbdesc.npy',dbdesc)

# Create index
FLANN_INDEX_ALGO=0
start = timer()
index_params = dict(algorithm = FLANN_INDEX_ALGO)   # for linear search
#index_params = dict(algorithm = FLANN_INDEX_ALGO, trees = 5) # for kdtree search
fl=cv.flann_Index(dbdesc,index_params)
end = timer()
print ('Indexing time: ' + str(end - start)+' seconds')
fl.save(output_dir+'_linear_index.dat')











