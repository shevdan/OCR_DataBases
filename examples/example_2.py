'''
Example of working with json module for parsing json
files obtained from the api
'''

import os
import json
import requests
from pprint import pprint

API_KEY = '0ec5c956c2f74b279cf52c0706dbe7cf'
ENDPOINT = 'https://westeurope.api.cognitive.microsoft.com/vision/v1.0/ocr'


def handler(DIR):
    '''
    handles all the images from the directory with images and saves
    recognized text in output.txt
    '''
    text = ''
    for filename in sorted(os.listdir(DIR)):
        if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"): 
            pathToImage = '{0}/{1}'.format(DIR, filename)
            results = get_text(pathToImage)
            text += parse_text(results)

    open('output.txt', 'w').write(text)

def parse_text(results):
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

def get_text(pathToImage):
    '''
    Accesses API to get json file containing recognized text
    '''
    print('Processing: ' + pathToImage)
    headers  = {
        'Ocp-Apim-Subscription-Key': API_KEY,
        'Content-Type': 'application/octet-stream'
    }
    params   = {
        'language': 'en',
        'detectOrientation ': 'true'
    }
    payload = open(pathToImage, 'rb').read()
    response = requests.post(ENDPOINT, headers=headers, params=params, data=payload)
    results = json.loads(response.content)
    #prints the json from the API
    pprint(results)
    return results

if __name__ == '__main__':
    # insert path to the folder with images here
    DIR = '/Users/shevdan/Documents/Programming/Python/semester2/GroupProject/TextRecognition/examples/images'
    handler(DIR)