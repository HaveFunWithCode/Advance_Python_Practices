import PIL
from PIL import Image, ImageFilter
import concurrent.futures
import os
import time

""" compare multi-processing and multi-threading in a io-bound task"""


def image_process(image_name, dir_path):
    image = Image.open(dir_path + image_name)
    image = image.filter(ImageFilter.GaussianBlur(15))
    image.thumbnail(size=(50, 50))
    image.save('processed/{}'.format(image_name))
    return 'in process_id :{}---->{} was processed '.format(os.getpid(), image_name)


def image_process_wrapper(p):
    return image_process(*p)


def process_with_multi_process(_image_names, _dir_path):
    args = ((_image_name, _dir_path) for _image_name in image_names)
    with concurrent.futures.ProcessPoolExecutor() as executer:
        results = executer.map(image_process_wrapper, args)
    for rs in results:
        print(rs)


def process_with_multi_thread(_image_names, _dir_path):
    args = ((_image_name, _dir_path) for _image_name in image_names)
    with concurrent.futures.ThreadPoolExecutor() as executer:
        results = executer.map(image_process_wrapper, args)
    for rs in results:
        print(rs)


def process_synchronous(_image_names, _dir_path):
    for image in _image_names:
        print(image_process(image, dir_path))


if __name__ == "__main__":
    dir_path = 'pics/'
    image_names = os.listdir(dir_path)

    print("---------process with multi-process---------------")
    start = time.perf_counter()
    process_with_multi_process(_image_names=image_names, _dir_path=dir_path)
    finish = time.perf_counter()
    print('total time is ...{}'.format(finish - start))

    print("---------process with multi-thread---------------")
    start = time.perf_counter()
    process_with_multi_thread(_image_names=image_names, _dir_path=dir_path)
    finish = time.perf_counter()
    print('total time is ...{}'.format(finish - start))

    print("---------process synchronous---------------")
    start = time.perf_counter()
    process_synchronous(_image_names=image_names, _dir_path=dir_path)
    finish = time.perf_counter()
    print('total time is ...{}'.format(finish - start))
