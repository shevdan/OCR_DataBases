

import zipfile, shutil, sys
import os
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image
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
    def __init__(self, dir_path) -> None:
        super().__init__(dir_path)

    def unzip_files(self):
        pass

    def process_folder(self):
        pass

    def zip_files(self):
        pass

    def create_csv(self, csv_path):
        df = pd.read_csv(csv_path)


    def convert_img_to_csv(self, img_path, df):
        '''
        Method converts an image into numpy array and adds it to csv file
        with a letter or ciffre on the front of the array as indicator of
        the symbol. Disclaimer: for expanding images for further ML learning
        Image must be a single image of hte symbol and to be contained in a
        folder which is called by the name of the symbol
        '''
        #read the image and convert it into 1d np array
        image = Image.open(str(img_path)).convert('RGBA')
        image = image.resize((28, 28), Image.ANTIALIAS)
        arr = np.array(image)
        flat_arr = arr.ravel()

        symb = str(img_path).split('/')[-2]
    
        if symb.isdigit():
            symb = int(symb)
        else:
            symb = ord(symb)
        print(symb)
        flat_arr = np.concatenate(([symb], flat_arr))
        # if not os.path.exists(csv_path):
        #     np.savetxt(csv_path, flat_arr, delimiter=',')
        # df = pd.read_csv(csv_path)

        df = pd.read_csv(df)
        print(len(list(df)))

        df.append(pd.DataFrame(flat_arr.reshape(1,-1), columns=list(df)), ignore_index=True)

        print(flat_arr)
        print(type(flat_arr))


if __name__ == '__main__':
    expand = CSVAugment('/Users/shevdan/Documents/Programming/Python/semester2/groupProject2/random')
    expand.convert_img_to_csv('/Users/shevdan/Documents/Programming/Python/semester2/groupProject2/Cyrillic/Б/5a96bd5286825.png', '/Users/shevdan/Documents/Programming/Python/semester2/groupProject2/train.csv')