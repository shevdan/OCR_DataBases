


"""
Module that implements ADT for operating with files and
expanding data needed for ML
"""

import sys, os
import abc


class AbstractAugment(metaclass=abc.ABCMeta):
    """
    ADT for operating with files and expanding data
    needed for ML
    """

    def __init__(self, dir_path: str):
        if not os.path.exists(dir_path):
            raise TypeError("Argument must be a valid path")
        self.fullpath = dir_path

    @abc.abstractmethod
    def unzip_files(self):
        raise NotImplementedError

    @abc.abstractmethod
    def process_folder(self, number_mult, dir_path):
        raise NotImplementedError

    @abc.abstractmethod
    def zip_files(self):
        raise NotImplementedError
