import numpy as np
import cv2


class DownScaler:
    def __init__(self, image, output_dir = None):
        """
        k: is the scaling factor (an integer) not a float
        image: is the directory of image to be rescaled
        output_dir: This is the directory to which the downscaled data is saved to
        """
        
        self.img = image
        self.output_dir = output_dir
        return

    
    def rescale(self, image):
 
        img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
 
        dim = img.shape
 
        width = int(dim[0]/2)
        height = int(dim[1]/2) # keep original height
        dim = (width, height)
 
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        file_name = image.split('.')[-2].spilt('/')[-1]
        image_dir = 
        if output_dir == None:
            name =  + '/' + file_name
        cv2.imwrite(name, resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
        return