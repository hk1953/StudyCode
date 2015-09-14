import os
import string
import random
import io
for i in xrange(1,100):
 f = None;
 try:
    f = open("file_"+str(i)+".txt", 'w')
    os.chdir('/home/mohitsharma44/Documents/project1/code1/')
    chars = string.letters + string.digits + string.punctuation
    line=''.join((random.choice(chars)) for x in range(50))
    f.write(line)
 except IOError, e:
    print 'Error performing I/O operations on the file: ',e
 finally:
    if f:
       f.close()
