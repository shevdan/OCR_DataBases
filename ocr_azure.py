
'''
Module implementing test ADT to use Microsoft Azure API
'''

import os
import json
from typing import Type
import requests


class OCR():
    '''
    ADT that enables text recognition of any amount of images stored in one directory.
    Takes path to the directory with stored images, name of the file to store the
    recognized text and optionally language of the recognition when created the instance of the ADT
    ...

    Class Attributes
    ----------------
    API_KEY
        string that contains secret key obligatory to use the Azure API
    ENDPOINT
        Another obligatory element to use API

    Attributes
    ----------
    img_directory
        directory where images are stored. Note: works even if there are other files except the images
        in the directory
    filename
        string that defines the name of the file that will contain the recognized text
    language
        optional parametr defining the text language to be recognized.
        Default value is 'en' for English. Possible values include: 'en', 
        'es', 'fr', 'de', 'it', 'nl', 'pt'. Azure OCR v. 3.2 is awaited to
        be implemented in the code to support over 70 languages in near future.
    headers
        dictionary that defines headers to get send requests from Azure API
    params
        dictionary containing parameters of the request to the API

    Methods
    -------
    get_text(pathToImage)
        sends request to the API and returns information from
        json converted into the python dictionary.
        Takes a full path to the image, which is got as concatenation
        of the directory + the name of the file inside the directory
    parse_text()
        parses the json and gets the text from the image.
    handler()
        iterates over each file within a directory, sends requests to the API
        to recognize text, gets the recognized text and saves it into the file.
    '''
    API_KEY = '0ec5c956c2f74b279cf52c0706dbe7cf'
    ENDPOINT = 'https://westeurope.api.cognitive.microsoft.com/vision/v1.0/ocr'

    def __init__(self, img_directory: str, output_file_name: str, language='en'):
        if not os.path.exists(img_directory):
            raise TypeError('Invalid path to the directory')
        self.img_directory = img_directory
        self.filename = output_file_name
        self.language = language
        self.headers  = {
            'Ocp-Apim-Subscription-Key': self.API_KEY,
            'Content-Type': 'application/octet-stream'
        }
        self.params   = {
            'language': self.language,
            'detectOrientation ': 'true'
        }

    def get_text(self, pathToImage):
        '''
        Accesses API to get json file containing recognized text
        '''
        payload = open(pathToImage, 'rb').read()
        response = requests.post(self.ENDPOINT, headers=self.headers, params=self.params, data=payload)
        results = json.loads(response.content)

        return results

    def parse_text(self, results):
        '''
        Parses the information from json file
        '''
        text = ''
        for region in results['regions']:
            for line in region['lines']:
                for word in line['words']:
                    text += word['text'] + ' '
                text += '\n'
        return text  

    def handler(self):
        '''
        handles all the images from the directory with images and saves
        recognized text in output.txt
        '''
        text = ''
        for filename in sorted(os.listdir(self.img_directory)):
            if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"): 
                pathToImage = f'{self.img_directory}/{filename}'
                results = self.get_text(pathToImage)
                text += self.parse_text(results)

        open(self.filename, 'w').write(text)


if __name__ == '__main__':
    ocr = OCR('/Users/shevdan/Documents/Programming/Python/semester2/GroupProject/TextRecognition/examples/images','output.txt')

