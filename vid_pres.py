import numpy as np
import skimage
from skimage.io import imread_collection

low_resolution = imread_collection('Superman vs Justice League _ Justice League (4K. HDR).mp4')
print('done')
low_resolution.