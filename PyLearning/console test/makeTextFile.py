#!/usr/bin/env python

'makeTextFilej.py--creat text file'

import os
ls=os.linesep
fname="makeTextFile.txt"
#get filename
while True:

    if os.path.exists(fname):
        print("Error:'%s' already exits" %fname)
    else:
        break

        # get file content (text) lines
all=[]
print("\nEnter license('.'by itself to quit).\n")
        # loop until user terminates input
while True:
    entry = input('input>')
    if entry =='.':
        break
    else:
        all.append(entry)

            #write lines to file with proper line-ending
fobj=open(fname,'w')
fobj.writelines(['%s%s'%(x,ls)for x in all])
fobj.close()
print('done')
