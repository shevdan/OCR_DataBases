import time

from image_augment import ImageAugment
from convert_csv import CSVConvert

def test_time_augment(path, num_mult):
    augment = ImageAugment(path)
    now = time.time()
    augment.extend(num_mult)
    dif = time.time() - now
    return dif

def test_csv_convert(path):
    extend = CSVConvert(path)
    now = time.time()
    extend.convert()
    dif = time.time() - now
    return dif

def test_img_augment(path1, path2):
    time_1 = test_time_augment(path1, 1)
    time_2 = test_time_augment(path2, 2)
    time_1_1 = test_time_augment(path1, 1)

    print(f'ImageAugment takes {round(time_1, 3)} seconds to operate over folder containing ~ 300 images \
and generate 1 image for each image')
    print(f'ImageAugment takes {round(time_1_1, 3)} seconds to operate over folder containing ~ 600 images \
and generate 1 image for each image')
    print(f'ImageAugment takes {round(time_2, 3)} seconds to operate over folder containing ~ 300 images \
and generate 2 images for each image')


def test_convert(path_small_csv, path_big_csv):
    time_1 = test_csv_convert(path_small_csv)
    time_2 = test_csv_convert(path_big_csv)
    print(f'CSVConvert takes {round(time_1, 3)} seconds to convert csv file containing 1000 images into images.')
    print(f'CSVConvert takes {round(time_2, 3)} seconds to convert csv file containing ~40000 images into images.')

if __name__ == '__main__':
    path_small = 'INSERT YOUR PATH TO CSV ARCHIVE HERE'
    path_big = 'INSERT YOUR PATH TO CSV ARCHIVE HERE'
    path_imgs = 'INSERT YOUR PATH TO IMAGES ARCHIVE HERE'
    path_imgs_2 = 'INSERT YOUR PATH TO IMAGES ARCHIVE HERE'
    print('Testing converting')
    test_convert(path_small, path_big)

    print('Testing extending images dataset')
    test_img_augment(path_imgs, path_imgs_2)