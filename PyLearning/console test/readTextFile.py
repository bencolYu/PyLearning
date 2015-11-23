#!/user/bin/env/ Python

'readTextfile.py-- read and display text'

# get filename
fname = input('Enter filename:')
print

#attempt to open file for reading
try:
    fobj = open(fname,'r')
except IOError as e:
    print ("file open error",format(e.errno, e.strerror))
else:
            #display contents to the screen
    for eachLine in fobj:
        print(eachLine),
    fobj.close()


