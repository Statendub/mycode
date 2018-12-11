#!/usr/bin/env python3
import shutil
import os
#these IMPORT commands will IMPORT the functions INTO Python env to allow usage
os.chdir('/home/student/mycode/')
#this allows the script here to be run from this directory 
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
shutil.copytree('5g_research/','5gresearch_backup/')


