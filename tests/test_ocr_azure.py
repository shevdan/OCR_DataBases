from typing import Type
import unittest, os
from ocr_azure import OCR

class TestOCR(unittest.TestCase):
    def setUp(self):
        self.ocr = OCR('../examples/images', 'output.txt', '3592a71759b9440c8824481a381347b9')
        self.res = self.ocr.get_text(f'{self.ocr.img_directory}/azurebeg.png')

    def test_init_(self):
        with self.assertRaises(TypeError):
            OCR('hi', 'wassup')
        with self.assertRaises(TypeError):
            OCR('hi')
        with self.assertRaises(TypeError):
            OCR()

    def test_get_text(self):
        self.assertIsInstance(self.ocr.get_text(f'{self.ocr.img_directory}/azurebeg.png'), dict)

    def test_parse_text(self):
        self.assertIsInstance(self.ocr.parse_text(self.res), str)
        self.assertEqual(self.ocr.parse_text(self.res), 'Microsoft Azure \n')

    def test_handler(self):
        self.assertIsInstance(self.ocr.handler(), str)
        self.assertEqual(self.ocr.handler(), "LEARN \nITALIAN \nPARALLEL TEXT \nParli \nEASY STORIES \
\nBILINGUAL \nTO TEXT: \nHOW TO \nEXTRACT TEXT \nFROM AN IMAGE \nMicrosoft Azure \n/owcpa.'t& aee \n")
        try:
            os.remove('output.txt')
        except (IsADirectoryError, FileNotFoundError):
            pass



if __name__ == '__main__':
    unittest.main()