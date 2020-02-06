import numpy as np
import cv2


class DownScaler:
    def __init__(self, k, image, output_dir = None):
        """
        k: is the scaling factor (an integer) not a float
        image: is the directory of image to be rescaled
        output_dir: This is the directory to which the downscaled data is saved to
        """
        self.k = k
        self.img = image
        self.output_dir = output_dir
        return

    def rescale(self):
        img = cv2.imread(self.img)
        x,y,z = img.shape
        new_scale = int(x/k), int(y/k), int(z/k)

        img_resized = img.resize(new_scale)
        # get image name from directory of the image to be transformed
        
        image_name = self.output_dir + image[]
        cv2.imwrite(img_resized, image_name)
        return