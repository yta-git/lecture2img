from os import mkdir
from os.path import exists
import cv2
from sys import argv

def mp4tojpg(mp4, odir='output_jpg', step=1):

    if not exists(odir):
        mkdir(odir)

    cap = cv2.VideoCapture(mp4)
    all = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    for num in range(1, int(all), int(fps) * step):
        cap.set(cv2.CAP_PROP_POS_FRAMES, num)
        output = f'./{odir}/{(num-1)//int(fps):05}.jpg'
        cv2.imwrite(output, cap.read()[1])
        print(f'\r({num}/{int(all)}) saved: {output}', end='')

    cap.release()
    

if __name__ == '__main__':
    tfile = argv[1]
    print(f'target file: {tfile}')
    mp4tojpg(tfile, step=5)