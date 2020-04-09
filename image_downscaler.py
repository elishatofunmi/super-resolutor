import numpy as np
import cv2
import os, sys

# Link to dataset: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html

class Imagescaling:
    def __init__(self, array_dir, output_dir = None):
        """
        array_dir: This is the directory to where all images to be transformed is.
        output_dir: This is the directory to which the downscaled image is saved to.
        """
        
        self.array_dir = array_dir
        self.output_dir = output_dir

        return


    def execute(self):
        os.chdir(self.array_dir)
        list_images = os.listdir()
        #[self.rescale(k) for k in list_images]
        
        count = 0
        for k in list_images:
            try:
                self.rescale(k)
            except AttributeError:
                continue
            finally:
                count+= 1

        print('transformed '+str(count)+' out of '+str(len(list_images)))
        return 'Finished!!!'

    
    def rescale(self, image):
 
        img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
 
        dim = img.shape
 
        width = int(dim[0]/2)
        height = int(dim[1]/2) # keep original height
        dim = (width, height)
 
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        #file_name = image.split('.')[-2].spilt('/')[-1]
        
        current_dir = os.getcwd()
        try:
            os.mkdir('rescaled_images')
            new_dir = current_dir + '/'+'rescaled_images'
            os.chdir(new_dir)
        except FileExistsError:
            pass
        finally:
            new_dir = current_dir + '/'+'rescaled_images'
            os.chdir(new_dir)
            cv2.imwrite(image, resized)
            os.chdir(current_dir)
            cv2.destroyAllWindows() 
        
        return True

if __name__ == '__main__':
    image_dir_train = '/home/odemakinde/Desktop/BSR_bsds500/BSR/BSDS500/data/images/train/High resolution'
    image_dir_test = '/home/odemakinde/Desktop/BSR_bsds500/BSR/BSDS500/data/images/test/High resolution'
    image_dir_validation = '/home/odemakinde/Desktop/BSR_bsds500/BSR/BSDS500/data/images/val/High resolution'
    #execute train
    im_scale = Imagescaling(array_dir = image_dir_train)
    im_scale.execute()

    #execute test
    im_scale = Imagescaling(array_dir = image_dir_test)
    im_scale.execute()

    #execute validation
    im_scale = Imagescaling(array_dir = image_dir_validation)
    im_scale.execute()