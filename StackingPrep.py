from os import listdir
from os.path import isfile, join, getmtime
from itertools import tee

# from itertools
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

filegroup = 1

fullpath = 'C:\\py\\StackingPrep\\'

files = [
	[f, getmtime(join(fullpath, f)), 0]
	for f in listdir(fullpath) 
	if isfile(join(fullpath, f)) and f.endswith('.txt') #change later
]

# Sort by modified timestamp
files.sort(key=lambda x: x[1])

# Group files together
for file, nextfile in pairwise(files):
	# if the next file's mtime is within 5 seconds, assign group. Otherwise, increment and assign group
	if nextfile[1] - file[1] < 6:
		file[2] = filegroup
		nextfile[2] = filegroup
	else:
		file[2] = filegroup
		filegroup += 1
		nextfile[2] = filegroup

for f in files:
	print(f)
