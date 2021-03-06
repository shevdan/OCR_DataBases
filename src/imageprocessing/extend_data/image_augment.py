
'''
This module is designed to expand the number of images that are intended
to be fed to ML. This is made by applying random changes to each image.
'''

import zipfile, shutil, sys
import sys,os
from pathlib import Path

import numpy as np
from PIL import Image
from imageio import imread
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator


from .data_adt import AbstractAugment

class ImageAugment(AbstractAugment):
    '''
    Class is designed to expand the number of images that are intended
    to be fed to ML. This is made by applying random changes to each image.

    Attributes
    ----------
    fullpath: `str`
        path to a zip file that contains images which will be multiplied.
        Currently it is necessary for the file to be an archive
    temp_drectory: `Path`
        Path of the temporary directory where all the files
        from the archive will be extracted

    Methods
    -------
    unzip_files()
        exctracts the zip file into the temporary directory
    augment_image(filename, number_mult)
        applies ImageDataGenerator and generate given number of randomly
        created images from the base one, which has the filename path
    process_folder(number_mult, dir_path)
        recursively walks through all the directories located by the dir_path
        and applies augment_image to every image
    zip_files()
        zips the file and removes the temporary directory
    '''
    def __init__(self, dir_path: str):
        AbstractAugment.__init__(self, dir_path)
        zipname = dir_path.split('/')
        zipname = zipname[-1]
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

    def augment_image(self, filename: str,  number_mult: int):
        '''
        applies ImageDataGenerator and generate given number of randomly
        created images from the base one, which has the filename path.
    
        Parameters
        ----------
        filename: `str`
            path to the image that is being taken as a base for generation
        number_mult: `int`
            number of generated images per image
        '''
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


    def process_folder(self,number_mult: int, dir_path):
        '''recursively walks through all the directories located by the dir_path
        and applies augment_image to every image.

        Parameters
        ----------
        number_mult: `int`
            number of generated images per image
        dir_path: Union[`str`, `Path`]
            path to the folder to operate
        '''
        if isinstance(dir_path, str):
            dir_path = Path(dir_path)
        for filename in dir_path.iterdir():
            if os.path.isdir(str(filename)):
                self.process_folder(number_mult, Path(str(filename)))
            else:
                if str(filename).endswith(".jpeg") or str(filename).endswith(".jpg") or str(filename).endswith(".png"): 
                    self.augment_image(str(filename), number_mult)

    def zip_files(self):
        '''
        zips the file and removes the temporary directory.
        '''
        dir_path = self.fullpath[:-4]

        shutil.make_archive(dir_path, 'zip', str(self.temp_directory))

        shutil.rmtree(str(self.temp_directory))

    def extend(self, number_mult):
        '''
        Method that enables to go through all the steps
        to unzip, extend and zip back images.
    
        Parameters
        ----------
        number_mult: `int`
            number of generated images per image
        '''
        self.unzip_files()
        self.process_folder(number_mult, self.temp_directory)
        self.zip_files()
