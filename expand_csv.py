import zipfile, shutil, sys
import os
from pathlib import Path

import numpy as np
from math import sqrt
from numpy.lib.arraysetops import isin
import pandas as pd
from PIL import Image, ImageOps
from imageio import imread
import matplotlib.pyplot as plt
from numpy.lib.type_check import imag
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import utils
from sklearn.model_selection import train_test_split
from data_adt import AbstractAugment


class CSVAugment(AbstractAugment):
    def __init__(self, dir_path, im_size=(28, 28), output=None) -> None:
        super().__init__(dir_path)
        direct = '/'.join(dir_path.split('/')[:-1])
        if output is None:
            self.output = Path(direct + '/train_images')
        else:
            self.output = Path(direct + '/' + output)
        self.im_size = im_size
        if not os.path.exists(str(self.output)):
            self.output.mkdir()

    def unzip_files(self):
        """
        exctracts the zip file into the temporary directory
        """
        try:
            self.output.mkdir()
        except FileExistsError:
            shutil.rmtree(str(self.output))
            self.output.mkdir()

        with zipfile.ZipFile(self.fullpath) as zip:
            zip.extractall(str(self.output))

    def process_folder(self, dir_path):
        """recursively walks through all the directories located by the dir_path
        and applies augment_image to every image"""
        if isinstance(dir_path, str):
            dir_path = Path(dir_path)
        for filename in dir_path.iterdir():
            if os.path.isdir(str(filename)):
                print(f'Processing {str(filename).split("/")[-1]}')
                self.process_folder(number_mult, Path(str(filename)))
            else:
                if os.path.isfile(str(filename)):
                    self.convert_csv_to_img(str(filename))
                    pass
                    # self.augment_image(str(filename), number_mult)

    def convert_csv_to_img(self, filename):
        """
        Method converts an image into numpy array and adds it to csv file
        with a letter or ciffre on the front of the array as indicator of
        the symbol. Disclaimer: for expanding images for further ML learning
        Image must be a single image of hte symbol and to be contained in a
        folder which is called by the name of the symbol
        """
        data = np.loadtxt(filename, skiprows=1, delimiter=',')
        i = 0
        for row in data:
            i += 1
            symb, pixels = row[0], row[1:]
            self.pixels_to_img(pixels, symb, i)
            if i == 10:
                break

    def pixels_to_img(self, pixels, symb, cnt):
        if 0 <= symb < 10:
            symb = str(symb)
        else:
            symb = chr(symb)
        print(pixels.size)
        # pixels = pixels.reshape(28, 28)
        pixels = pixels.reshape(int(sqrt(pixels.size)), int(sqrt(pixels.size)))
        image = Image.fromarray(pixels)
        image.resize(self.im_size)
        image = image.convert("L")
        image.show()
        symb_directory = str(self.output) + '/' + symb

        img_name = f'{symb_directory}/{symb}_{cnt}.png'
        if not os.path.isdir(symb_directory):
            Path(symb_directory).mkdir()
        image.save(img_name)

    def zip_files(self):
        # dir_path = self.fullpath[:-4]
        # root_dir = '/'.join(str(self.temp_directory).split('/')[:-1])
        # print(dir_path,'\n',  root_dir)
        shutil.make_archive(str(self.output), 'zip', str(self.output))
        shutil.rmtree(str(self.temp_directory))
