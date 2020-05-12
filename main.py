import mp4tojpg
import affine
import check_same
from sys import argv

# python main.py lecture.mp4 output

tfile = argv[1]
odir = argv[2]
print(f'target file: {tfile}')
print(f'output dir: {odir}')

mp4tojpg.mp4tojpg(tfile, odir='output_jpg', step=5)
affine.affine_run('output_jpg', odir='output_affine')
check_same.simples('output_affine', odir=odir)