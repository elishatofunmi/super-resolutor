import cv2
import numpy as np
#% matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from PIL import Image
import argparse
import os
import sys



def transform(img,k=2):
   
    m, n, o = img.shape
  # make a copy of the image
    copy_image = img.copy()

  # transforming the image of channel one (1)
    channel_one = copy_image[:,:,0]
    channel_two = copy_image[:,:,1]
    channel_three = copy_image[:,:,2]

    # create dummy array of zeros for each channel
    new_channel_one = np.zeros((k*m,k*n))
    new_channel_two = np.zeros((k*m,k*n))
    new_channel_three = np.zeros((k*m,k*n))

    # iterate each row and column from the image to be magnified for channel 1
    for m,c in enumerate(channel_one):
        for n,b in enumerate(c):
            i,j = 0,0
            i,j = m*k, n*k
            # reinitialize the 3 k nearest neighbor present in the new 2 by 2 matrix
            # give them same value for every corresponding channel.
            new_channel_one[i][j] = b # a22
            new_channel_one[i-1][j-1] = b #a11
            new_channel_one[i-1][j] = b #a12
            new_channel_one[i][j-1] = b #a21
    # iterate each row and column from the image to be magnified for channel 2
    for m,c in enumerate(channel_two):
         for n,b in enumerate(c):
            i,j = 0,0
            i,j = m*k, n*k
            # reinitialize the 3 k nearest neighbor present in the new 2 by 2 matrix
            # give them same value for every corresponding channel.
            new_channel_two[i][j] = b # a22
            new_channel_two[i-1][j-1] = b #a11
            new_channel_two[i-1][j] = b #a12
            new_channel_two[i][j-1] = b #a21

    # iterate each row and column from the image to be magnified for channel 3
    for m,c in enumerate(channel_three):
         for n,b in enumerate(c):
            i,j = 0,0
            i,j = m*k, n*k
            # reinitialize the 3 k nearest neighbor present in the new 2 by 2 matrix
            # give them same value for every corresponding channel.
            new_channel_three[i][j] = b # a22
            new_channel_three[i-1][j-1] = b #a11
            new_channel_three[i-1][j] = b #a12
            new_channel_three[i][j-1] = b #a21

    # return the newly transformed channels
    return new_channel_one, new_channel_two, new_channel_three




if __name__ == '__main__':
    #specify directory to the input image
#    image_dir = "/desktop/image/images.jpeg
    base_dir = 'desktop/image'
    imagename = sys.argv[1]
    image_dir = os.path.join(base_dir, imagename)
    image_n = imagename.split('.')[0]
    output_dir = os.path.join('desktop/output/', '{}.png'.format(imagename))


    #pass in image directory into matplotlib image library reader
    img=pltimg.imread(image_dir)
    
    #display shape of image
    print(img.shape)
    m, n, o = img.shape

    #make a copy of image
    copy_image = img.copy()

    #call the transformer function
    c1, c2, c3 = transform(copy_image, k=2) #returns RGB index 0,1,2 as a tuple of arrays
    k  = 2
    # create a dummy RGB array of dimension k*m by k*n by 3
    array = np.zeros([k*m,k*n, 3], dtype=np.uint8)
    array[:,:,0] = c1 #assign R
    array[:,:,1] = c2 # assign G
    array[:,:,2] = c2 # assign B

    save_img = Image.fromarray(array)
    save_img.save(output_dir)
