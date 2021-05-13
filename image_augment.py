
import zipfile, shutil, sys
from os import path
from pathlib import Path

import numpy as np
from PIL import Image
from imageio import imread
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import utils
from sklearn.model_selection import train_test_split

class ImageAugment:
    def __init__(self, dir_path: str):
        if not path.exists(dir_path):
            raise TypeError("Argument must be a valid path")
        self.fullpath = dir_path
        zipname = dir_path.split('/')
        zipname = zipname[-1]
        self.zipname = zipname
        self.temp_directory = Path(f"unzipped-{zipname[:-4]}")

    def unzip_files(self):
        '''
        exctracts the zip file into the temporary directory
        '''
        try:
            self.temp_directory.mkdir()
        except FileExistsError:
            shutil.rmtree(str(self.temp_directory))
            self.temp_directory.mkdir()

        with zipfile.ZipFile(self.fullpath) as zip:
            zip.extractall(str(self.temp_directory))

    def augment_image(self, filename,  number_mult):
        # extract the path to the folder 
        folder = '/'.join(filename.split('/')[:-1])
        # read the image into a numpy array

        image = np.expand_dims(imread(str(filename)), 0)
        # create datagenetator
        datagen = ImageDataGenerator(
            rotation_range = 10,
            zoom_range = 0.1,
            brightness_range=[0.1, 1],
            width_shift_range = 0.1,
            height_shift_range = 0.1
        )
        datagen.fit(image)
        for x, val in zip(datagen.flow(image,                    #image we chose
            save_to_dir=folder,     #this is where we figure out where to save
            save_prefix='aug',        # it will save the images as 'aug_0912' some number for every new augmented image
            save_format='png'),range(number_mult)) :     # here we define a range because we want 10 augmented images otherwise it will keep looping forever I think
            pass


    def process_zip(self,number_mult, dir_path):
        '''Iterates over the folders in a zip file and  augments each png file'''
        for filename in dir_path.iterdir():
            if path.isdir(str(filename)):
                print(f'Processing {str(filename).split("/")[-1]}')
                self.process_zip(number_mult, Path(str(filename)))
            else:
                self.augment_image(str(filename), number_mult)

    def zip_files(self):
        '''
        zips the file and removes the remporary directory
        '''
        with zipfile.ZipFile(self.fullpath, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))

    
if __name__ == '__main__':
    import scipy
    augm = ImageAugment('/Users/shevdan/Documents/Programming/Python/semester2/GroupProject/Cyrillic.zip')
    print(augm.fullpath)
    print(augm.zipname)
    print(scipy.__version__)
    augm.unzip_files()
    augm.process_zip(2, augm.temp_directory)
    augm.zip_files()
    # augm.augment_image('/Users/shevdan/Documents/Programming/Python/semester2/GroupProject/random/5a2f3c19c27bb.png', 10)