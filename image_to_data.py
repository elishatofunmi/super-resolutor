import cv2
import numpy as np
import os
import skimage
import matplotlib.pyplot as plt

os.chdir('/home/odemakinde/Desktop/super-resolutor-master/data_source')


high_resolution = cv2.VideoCapture('./Superman vs Justice League _ Justice League (4K. HDR)(1).mp4')
low_resolution = cv2.VideoCapture('./Superman vs Justice League _ Justice League (4K. HDR).mp4')

high_length = int(high_resolution.get(cv2.CAP_PROP_FRAME_COUNT))
low_length = int(low_resolution.get(cv2.CAP_PROP_FRAME_COUNT))

print('video lengths are: %d, %d'%(high_length, low_length))
print(os.listdir())
cam = high_resolution
try: 
	
	# creating a folder named data 
	if not os.path.exists('train input'): 
		os.makedirs('data') 

# if not created then raise error 
except OSError: 
	print ('Error: Creating directory of data') 

# frame 
currentframe = 0


if (cam.isOpened() == False):
    print('Error Opening Video File')
while not cam.isOpened():
    cam = cv2.VideoCapture("./Superman vs Justice League _ Justice League (4K. HDR)(1).mp4")
    cv2.waitKey(1000)
    print('wait for the header')

pos_frame = cam.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
while (True):
    ret, frame = cam.read()
    print(ret)
    if ret:
        name = './data/frame'+ str(currentframe) + '.jpg'
        print('creating...'+ frame)
        cv2.imwrite(name,frame)
        currentframe +=1
    else:
        break



# # Release all space and windows once done 
cam.release() 
