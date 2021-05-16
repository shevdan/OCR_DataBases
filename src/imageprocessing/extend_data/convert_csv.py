"""
Module that enables processing csv files
that contain images to be converted to images
"""

import zipfile, shutil, sys
import sys,os
sys.path.append(os.getcwd())
from pathlib import Path

import numpy as np
from math import sqrt
from PIL import Image, ImageOps

from .data_adt import AbstractAugment





class CSVConvert(AbstractAugment):
    """
    Class that enables processing csv files
    that contain images to be converted to images
    CSV file must be archived in order to process it

    Attributes
    ----------
    fullpath: `str`
        path to the archive containing csv files
        ! Note ! Correct output will be proceeded for csv file that
        contains an image unicode character at the first column
        and pixels for the rest of columns
    im_size: `tuple`
        tuple that contains size of the image that will be saved.
        Default value is 28x28 size
    output: `str`
        name of the archive with images that will be created in the same
        directory as csv archive. Default value is train_images

    Methods
    -------
    unzip_files()
        exctracts the zip file into the temporary directory
    process_files(dir_str)
        recursively walks through all the directories located by the dir_path
        and converts each array containing image in csv into an image
    convert_csv_to_image(filename)
        Method converts a numpy array into an image and
        saves it into the folder named by the symbol
        of the image in a output_file directory.
        ! Note ! Correct output will be proceeded for csv file that
        contains an image unicode character at the first column
        and pixels of the square image for the rest of columns
    pixels_to_img(pixels, symb, cnt)
        converts one numpy array into an image and saves it into
        the folder named by the symbol
        of the image in a output_file directory
    convert()
        Method that processes the archive containing csv,
        processes images in there and archives foler with images

    """
    def __init__(self, fullpath: str, im_size=(28,28), output='train_images') -> None:
        super().__init__(fullpath)
        dir_path = '/'.join(fullpath.split('/')[:-1])
        self.output = Path(f'{dir_path}/{output}')
        self.im_size = im_size
        self.unzipped = Path(f'{dir_path}/unzipped')
        if not os.path.exists(str(self.output)):
            self.output.mkdir()

    def unzip_files(self):
        """
        exctracts the zip file into the temporary directory
        """
        try:
            self.unzipped.mkdir()
        except FileExistsError:
            shutil.rmtree(str(self.unzipped))
            self.unzipped.mkdir()

        with zipfile.ZipFile(self.fullpath) as zip:
            zip.extractall(str(self.unzipped))

    def process_folder(self, dir_path):
        """recursively walks through all the directories located by the dir_path
        and converts each array containing image in csv into an image"""
        if isinstance(dir_path, str):
            dir_path = Path(dir_path)
        for filename in dir_path.iterdir():
            if os.path.isdir(str(filename)):
                print(f'Processing {str(filename).split("/")[-1]}')
                self.process_folder(Path(str(filename)))
            else:
                if os.path.isfile(str(filename)):
                    self.convert_csv_to_img(str(filename))


    def convert_csv_to_img(self, filename: str):
        '''
        Method converts a numpy array into an image and
        saves it into the folder named by the symbol
        of the image in a output_file directory.
        ! Note ! Correct output will be proceeded for csv file that
        contains an image unicode character at the first column
        and pixels of the square image for the rest of columns
    
        Parameters
        ----------
        filename: `str`
            path to the csv file to be converted into the folder with images
        '''
        data = np.loadtxt(filename, skiprows=1, delimiter=',')
        counter = 0
        for row in data:
            counter += 1
            symb, pixels = row[0], row[1:]
            self.pixels_to_img(pixels, symb, counter)



    def pixels_to_img(self, pixels: np.ndarray, symb: str, cnt: int):
        '''
        converts one numpy array into an image and saves it into
        the folder named by the symbol
        of the image in a output_file directory
    
        Parameters
        ---------
        pixels: `np.ndarray`
            1-dimensional numpy array containing pixels of an image
        symb: `str`
            symbol of the image
        cnt: `int`
            counter of the image in order for image to be named properly
        '''
        if 0 <= symb < 10:
            symb = str(symb)
        else:
            symb = chr(symb)

        pixels = pixels.reshape(int(sqrt(pixels.size)), int(sqrt(pixels.size)))
        image = Image.fromarray(pixels)
        image.resize(self.im_size)
        image = image.convert("L")

        symb_directory = f'{str(self.output)}/{symb}'

        img_name = f'{symb_directory}/{symb}_{cnt}.png'
        if not os.path.isdir(symb_directory):
            Path(symb_directory).mkdir()
        image.save(img_name)

    def zip_files(self):
        """
        zips the file and removes the temporary directory
        """
        shutil.make_archive(str(self.output), 'zip', str(self.output))
        shutil.rmtree(str(self.unzipped))
        shutil.rmtree(str(self.output))

    def convert(self):
        """
        Method that processes the archive containing csv,
        processes images in there and archives foler with images
        """
        self.unzip_files()
        self.process_folder(self.unzipped)
        self.zip_files()
