# file: the file in computer, if not exist >>> exception + stop
# file object: python file, will open a line of communication between Python and the file, only flow from computer to python

# raw bytes: bytes
# decoded text: str   t: open in text mode
# b: binary data

# r: read. default value
# w: writing, erases any previous content
# a: writing, append at the end of the file

# don't forget to close the file: file.close()
import os
import toolkit_config as cfg

SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')

fobj = open(SRCFILE,mode='r')
cnts = fobj.read()
print(cnts[:35])
print(fobj.closed)
fobj.close()
print(fobj.closed)

fobj = open(SRCFILE,mode='r')
cnts = ''
cnts_copy = ''
for line in fobj:
    cnts_copy += line
print(f'First 20 characteristics in cnts_copy:"{cnts_copy[:20]}"')
fobj.close()

# first_line = next(fobj)
# next() is a built-in Python function used for advancing an iterator (in this case, the file object) to the next item in the sequence.

def print_lines(pth):
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
# The enumerate function is used in a for loop to iterate over a sequence (such as a list, tuple, or file object)
# while keeping track of the index (or position) of the current item in the sequence.
# It is commonly used in scenarios where you want to process both the index and the item in the sequence simultaneously.
            print(f"line {i}: {line.rstrip()}")
# This will create the file located at `DSTFILE` and write some content to it
with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line\n')
    fobj.write('This is another line')
print_lines(DSTFILE)


