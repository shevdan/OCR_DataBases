"""
Module that is an example of Microsoft Azure Cognitive Services Api
to recognize textсу
"""

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.operations import ComputerVisionClientOperationsMixin

from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = "0ec5c956c2f74b279cf52c0706dbe7cf"
endpoint = "https://ucurecognition.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


def authenticate_cv_client(subscription_key: str, endpoint: str):
    """
    Authenticate
    Authenticates your credentials and creates a client.
    """
    return ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


def local_image_text_recognition(computervision_client, image_path: str, language='en'):
    """
    Text recognition from a image stored locally.
    Supported languages - Currently, only English ('en'), Dutch (‘nl’),
    French (‘fr’), German (‘de’), Italian (‘it’), Portuguese (‘pt),
    and Spanish ('es') are supported. Read supports auto language
    identification and multi-language documents, so only provide a l
    anguage code if you would like to force the documented to be
    processed as that specific language. Possible values include: 'en',
    'es', 'fr', 'de', 'it', 'nl', 'pt'
    Default value is 'en'
    Supports handwritten text recognition in english only
    """
    # Transform the image into the bytes array
    image = open(image_path, 'rb')
    # Call API with URL and raw response (allows you to get the operation location)
    if language != 'en':
        recognize_local_results = computervision_client.read_in_stream(image, language=language, raw=True)
    else:
        recognize_local_results = computervision_client.read_in_stream(image, raw=True)

    # Get the operation location (URL with an ID at the end) from the response
    operation_location_remote = recognize_local_results.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = operation_location_remote.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results 
    while True:
        get_handw_text_results = computervision_client.get_read_result(operation_id)
        if get_handw_text_results.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Print the detected text, line by line
    text = ''
    if get_handw_text_results.status == OperationStatusCodes.succeeded:
        for text_result in get_handw_text_results.analyze_result.read_results:
            for line in text_result.lines:
                text = text + line.text + '\n'

    return text


def url_image_text_recognition(computervision_client, image_url: str, language='en'):
    """
    Text recognition from a image url.
    Supported languages - Currently, only English ('en'), Dutch (‘nl’),
    French (‘fr’), German (‘de’), Italian (‘it’), Portuguese (‘pt),
    and Spanish ('es') are supported. Read supports auto language
    identification and multi-language documents, so only provide a l
    anguage code if you would like to force the documented to be
    processed as that specific language. Possible values include: 'en',
    'es', 'fr', 'de', 'it', 'nl', 'pt'
    Default value is 'en'.
    Supports handwritten text recognition in english only
    """
    print("===== Batch Read File - remote =====")

    # Call API with URL and raw response (allows you to get the operation location)
    if language != 'en':
        recognize_handw_results = computervision_client.read(image_url, language=language, raw=True)
    else:
        recognize_handw_results = computervision_client.read(image_url, raw=True)

    # Get the operation location (URL with an ID at the end) from the response
    operation_location_remote = recognize_handw_results.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = operation_location_remote.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results 
    while True:
        get_handw_text_results = computervision_client.get_read_result(operation_id)
        if get_handw_text_results.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Find the detected text, line by line
    text = ''
    if get_handw_text_results.status == OperationStatusCodes.succeeded:
        for text_result in get_handw_text_results.analyze_result.read_results:
            for line in text_result.lines:
                text = text + line.text + '\n'

    return text.strip()


def save_text(file_name: str, text: str, output_format: str):
    with open(file_name + '.' + output_format, 'w') as file:
        file.write(text)
