# OCR DataBases
# Description
[Homework Tasks](https://github.com/shevdan/OCR_DataBases/wiki)

Our project has two main features:
1. Reading text from an image

This feature simplifies the process of retrieving text from a picture, or rather makes it automatic to save user's time and reduce the probability of mistakes during text rewriting. The program receives the image from the user, and as a result displays the text and saves it to the file.

2. Increasing the database for further machine learning

The feature is created for developers, who need to expand the database with handwritten text, so that in the future, using machine learning, the program can also decrypt handwritten texts in many languages.

# Table of Contents
* [Installation](https://github.com/shevdan/OCR_DataBases#installation)
* [Usage for Text Recognition](https://github.com/shevdan/OCR_DataBases#usage-for-text-recognition)
* [Usage for Data Bases Extension](https://github.com/shevdan/OCR_DataBases#usage-for-data-bases-extension)
* [Contributing](https://github.com/shevdan/OCR_DataBases#contributing)
* [Credits](https://github.com/shevdan/OCR_DataBases#credits)
* [License](https://github.com/shevdan/OCR_DataBases#license)
# Installation
* Downloading and installing package from testpypi:
Write in terminal
```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple OCR_DataBases
```
Now you can use module  by accessing it via any of these examples
```
>>> import imageprocessing
>>> import imageprocessing.extend_data
>>> import imageprocessing.extend_data.convert_csv
>>> import imageprocessing.text_recognition
```
And basically use the package under the license agreement

* Alternively, you can do following:
```
   $ git clone https://github.com/shevdan/OCR_DataBases.git \
   $ cd OCR_DataBases \
   $ pip install -r requirements.txt
```
# Usage for Text Recognition
To use our text recognition you have to:
1. install the distributive.

2. Import modules as following:
   ```
   >>> import imageprocessing.text_recognition
   ```
   Alternatively:
   in module ocr_azure.py create an object of OCR() class with 3 (4 - optional) attributes: 
   * the path to the folder with your images
   * the name of the file you want the text to be in
   * api key to microsoft azure API
   * language - optional (english - default)
# Usage for Data Bases Extension
To receive the extension of your database you have to:
1. install the distributive.
2. Import modules as following:
   ```
   >>> import imageprocessing.extend_data
   ```
   Alternatevely:
   in module image_augment.py create an object of ImageAugment() class with 1 attribute:
   * the path to the zipfile with your database.
# Program modules 
The description of all the program modules you can find [here](https://github.com/shevdan/OCR_DataBases/wiki/Program-modules).
# Contributing

Pull requests are welcome. \
For major changes, please open an issue first to discuss what you would like to change.

To create a pull request:

* Fork this repository on GitHub 
* Clone the project to your computer 
* Create a new branch 
* Commit changes to your own branch
* Push your work back up to your forked repository
* Create a pull request so that we can review your changes
# Credits
* [Shevchuk Bohdan](https://github.com/shevdan)
* [Nahorniuk Marta](https://github.com/martazavro)
* [Smoliar Solomiya](https://github.com/SolomiyaSmoliar)
* [Zavoyko Ketrin](https://github.com/kthrnzvk)
* [Oleksandra Stasiuk](https://github.com/oleksadobush)
# License
[MIT License](https://choosealicense.com/licenses/mit/)
