from os import mkdir
from os.path import basename, exists
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
from glob import glob
from shutil import copyfile


def check_same(image1, image2, th=300):

    img1 = cv2.imread(image1, cv2.COLOR_RGB2GRAY)
    img2 = cv2.imread(image2, cv2.COLOR_RGB2GRAY)

    diff = cv2.absdiff(img1, img2)
    diff[diff < 128] = 0
    diff[diff >= 128] = 255

    # cv2.imshow('a', diff)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return sum(sum(sum(diff))) < th

def simples(tdir, odir, th=300):

    if not exists(odir):
        mkdir(odir)

    fls = sorted(glob(f'./{tdir}/*.jpg'))

    for f1, f2 in zip(fls, fls[1:]):
        if not check_same(f1, f2, th):
            print(f1, f2)
            copyfile(f1, f'./{odir}/{basename(f1)}')
            print(f'copied: {f1}')


if __name__ == '__main__':
    print(f'target dir: {argv[1]}')
    print(f'output dir: {argv[2]}')
    simples(argv[1], argv[2], 5)