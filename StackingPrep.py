from os import listdir
from os.path import isfile, join, getmtime

fullpath = 'C:\\py\\StackingPrep\\'

files = [
	[f, getmtime(join(fullpath, f))]
	for f in listdir(fullpath) 
	if isfile(join(fullpath, f))
]

for k, v in enumerate(files):
	print('File {}: {} modified at {}'.format(k, v[0], v[1]))