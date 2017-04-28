import collections
from os import listdir, stat, mkdir
from os.path import isfile, join, getmtime
from itertools import tee
from shutil import move

# from itertools
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def getGroupCount(iterable, grp):
	a = iterable
	counter = collections.Counter(a)
	print(counter)

timing = 4
filegroup = 1

fullpath = 'C:\\py\\StackingPrep\\'

files = [
	[f, getmtime(join(fullpath, f)), 0, join(fullpath, f), '']
	for f in listdir(fullpath) 
	if isfile(join(fullpath, f)) and f.endswith('.txt') #change later
]

if not files:
	print('No files to work on. Load files to root folder with this script in it. We out!')
	quit()

# Sort by modified timestamp
files.sort(key=lambda x: x[1])

# Group files together
for file, nextfile in pairwise(files):
	# if the next file's mtime is within 5 seconds, assign group. Otherwise, increment and assign group
	if nextfile[1] - file[1] < timing:
		file[2] = filegroup
		file[4] = join(fullpath, str(filegroup), file[0])
		nextfile[2] = filegroup
		nextfile[4] = join(fullpath, str(filegroup), nextfile[0])
	else:
		file[2] = filegroup
		file[4] = join(fullpath, str(filegroup), file[0])
		filegroup += 1
		nextfile[2] = filegroup
		nextfile[4] = join(fullpath, str(filegroup), nextfile[0])

print('-----------------------\n')
print('# Stack Prepation 0.1 #')
print('-----------------------\n')
print('Current timing: {} seconds'.format(timing))
print('Input images: {}'.format(len(files)))
print('Output images: {}'.format(filegroup))

for i in range(filegroup):
	# create a directory for each 
	directory = join(fullpath, '{}'.format(i+1))
	try:
		stat(directory)
	except:
		mkdir(directory)
		print('Creating directory: {}'.format(directory))

# Move dem files
for file in files:
	source = file[3]
	destination = file[4]
	move(source, destination)
	print('Moved {} to {} ...'.format(
		source
		, destination))