from os import mkdir
from os.path import basename, exists
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
from glob import glob

def find_area(image, area_th=50000):

    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area_th < area:
            epsilon = 0.1 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            areas.append(approx)

    return areas[0]

def affine(image, area, odir='output_affine', dist_size=(640, 450)):

    if not exists(odir):
        mkdir(odir)

    img = cv2.imread(image)

    dst = []
    pts1 = np.float32(area)
    pts2 = np.float32([[0,0],[0, dist_size[1]], [dist_size[0], dist_size[1]], [dist_size[0], 0]])
    Mat = cv2.getPerspectiveTransform(pts1,pts2)

    output_img = cv2.warpPerspective(img, Mat, dist_size)
    output_name = f'./{odir}/{basename(image).split(".")[0]}_affine.jpg'
    cv2.imwrite(output_name, output_img)
    print(f'\rsaved: {output_name}', end='')

def affine_run(tdir, odir='output_affine'):
    print(f'target dir: {tdir}')

    for f in glob(f'./{tdir}/*.jpg'):
        area = find_area(f)
        if len(area) == 4:
            break

    for f in glob(f'./{tdir}/*.jpg'):
        affine(f, area, odir=odir)



if __name__ == '__main__':
    tdir = argv[1]
    print(f'target dir: {tdir}')

    for f in glob(f'./{tdir}/*.jpg'):
        area = find_area(f)
        if len(area) == 4:
            break

    for f in glob(f'./{tdir}/*.jpg'):
        affine(f, area)

