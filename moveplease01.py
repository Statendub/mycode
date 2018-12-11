#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/mycode/')
shutil.move('raynor.obj','ceph_storage/')
#shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location. If destination points to a folder, the source file gets moved into destination and keeps its current filename
xname=input('what is the new name for kerrifan.obj?')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/'+xname)
## The xname will rename the file , then the SHUTIL.MOVE moves file with new name to DST folder)
