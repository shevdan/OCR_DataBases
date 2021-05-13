
import zipfile, shutil, sys
import os
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
        if not os.path.exists(dir_path):
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
            if os.path.isdir(str(filename)):
                print(f'Processing {str(filename).split("/")[-1]}')
                self.process_zip(number_mult, Path(str(filename)))
            else:
                try:
                    self.augment_image(str(filename), number_mult)
                except AttributeError:
                    continue

    def zip_files(self):
        '''
        zips the file and removes the remporary directory
        '''
        # zipf = zipfile.ZipFile(self.fullpath, 'w', zipfile.ZIP_DEFLATED)

        # for root, dirs, files in os.walk(str(self.temp_directory)):
        #     # root = root.split('/')
        #     # root[0] = root[0].split('-')
        #     # root[0] = root[0][-1]
        #     # root = '/'.join(root)
        #     print(root, dirs, files)
        #     print(type(root))
        #     for file in files:
        #         zipf.write(os.path.join(root, file), 
        #                 os.path.relpath(os.path.join(root, file), 
        #                                 os.path.join(str(self.temp_directory), '..')))
        # zipf.close()

        dir_path = self.fullpath[:-4]
        root_dir = '/'.join(str(self.temp_directory).split('/')[:-1])
        print(dir_path,'\n',  root_dir)
        shutil.make_archive(dir_path, 'zip', str(self.temp_directory))

        # d = str(self.temp_directory)

        # os.chdir(os.path.dirname(d))
        # with zipfile.ZipFile(dir_path + '.zip',
        #                     "w",
        #                     zipfile.ZIP_DEFLATED,
        #                     allowZip64=True) as zf:
        #     for root, _, filenames in os.walk(os.path.basename(d)):
        #         for name in filenames:
        #             name = os.path.join(root, name)
        #             name = os.path.normpath(name)
        #             zf.write(name, name)
        shutil.rmtree(str(self.temp_directory))

    
if __name__ == '__main__':
    import scipy
    from pathlib import Path
    augm = ImageAugment('/Users/shevdan/Documents/Programming/Python/semester2/groupProject2/random.zip')
    print(augm.fullpath)
    print(augm.zipname)
    print(scipy.__version__)
    augm.unzip_files()
    augm.process_zip(2, augm.temp_directory)
    augm.zip_files()
    # augm.augment_image('/Users/shevdan/Documents/Programming/Python/semester2/GroupProject/random/5a2f3c19c27bb.png', 10)
    # augm.process_zip(2, Path('/Users/shevdan/Documents/Programming/Python/semester2/GroupProject/random'))
    # augm.augment_image(None, 2)